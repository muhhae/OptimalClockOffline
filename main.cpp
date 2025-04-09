#include "lib/CLI11.hpp"
#include "lib/cache_size.h"

#include <algorithm>
#include <cstdlib>
#include <cstring>
#include <filesystem>
#include <fstream>
#include <future>
#include <iostream>
#include <libCacheSim/cache.h>
#include <libCacheSim/const.h>

#include <cmath>
#include <cstddef>
#include <cstdint>
#include <cstdio>
#include <libCacheSim/enum.h>
#include <libCacheSim/reader.h>
#include <sstream>
#include <string>
#include <sys/types.h>
#include <unistd.h>
#include <unordered_map>
#include <unordered_set>
#include <vector>

#include "libCacheSim.h"

const std::string csv_header =
    "trace_path,cache_size(MiB),miss_ratio,n_req,n_promoted\n";

struct obj_metadata {
  uint64_t access_counter = 0;
  uint64_t last_promotion = 0;
  std::unordered_set<uint64_t> wasted_promotions;
};

thread_local uint64_t n_hit = 0;
thread_local uint64_t n_req = 0;
thread_local uint64_t n_promoted = 0;
thread_local std::unordered_map<obj_id_t, obj_metadata> objs_metadata;

void clock_custom_evict(cache_t *cache, const request_t *req) {
  Clock_params_t *params = (Clock_params_t *)cache->eviction_params;
  cache_obj_t *obj_to_evict = params->q_tail;
  bool exist = false;
  while (obj_to_evict->clock.freq >= 1) {
    exist = false;
    auto &data = objs_metadata[obj_to_evict->obj_id];
    if (data.wasted_promotions.find(data.access_counter) !=
        data.wasted_promotions.end()) {
      exist = true;
      break;
    }
    data.last_promotion = data.access_counter;
    obj_to_evict->clock.freq -= 1;
    params->n_obj_rewritten += 1;
    params->n_byte_rewritten += obj_to_evict->obj_size;
    move_obj_to_head(&params->q_head, &params->q_tail, obj_to_evict);
    n_promoted++;
    obj_to_evict = params->q_tail;
  }
  if (!exist) {
    auto &data = objs_metadata[obj_to_evict->obj_id];
    data.wasted_promotions.insert(data.last_promotion);
  }
  remove_obj_from_list(&params->q_head, &params->q_tail, obj_to_evict);
  cache_evict_base(cache, obj_to_evict, true);
}

void RunClockExperiment(reader_t *reader, const std::filesystem::path log_dir,
                        const std::filesystem::path datasets_dir,
                        const uint64_t cache_size,
                        const std::string output_suffix,
                        const uint64_t max_iteration = 10) {

  request_t *req = new_request();
  cache_t *cache;

  cache = Clock_init({.cache_size = cache_size}, NULL);
  cache->evict = clock_custom_evict;

  std::string base_path =
      "/" + std::filesystem::path(reader->trace_path).string();
  size_t pos = base_path.find(".oracleGeneral");
  if (pos != std::string::npos) {
    base_path = base_path.substr(0, pos);
  }
  std::filesystem::path log_path =
      log_dir / (base_path + "_" + output_suffix + ".csv");

  std::ofstream csv_file(log_path);
  csv_file << csv_header;

  printf("\n\
============\n\
---start!---\n\
trace_path: %s\n\
cache_size: %lld\n\
iteration: %ld\n\
log: %s\n\
============\n",
         reader->trace_path, cache_size / MiB, max_iteration, log_path.c_str());

  uint64_t first_promoted = 0;
  std::vector<uint64_t> promotions;
  std::vector<double> miss_ratios;

  for (size_t i = 0; i < max_iteration; ++i) {
    n_hit = 0;
    n_req = 0;
    n_promoted = 0;

    while (read_one_req(reader, req) == 0) {
      objs_metadata[req->obj_id].access_counter += 1;
      if (cache->get(cache, req)) {
        n_hit++;
      }
      n_req++;
    }

    miss_ratios.push_back(1 - (double)n_hit / n_req);
    promotions.push_back(n_promoted);
    std::ostringstream s;
    s << "\"" << reader->trace_path << "\"," << cache_size / MiB << ","
      << 1 - (double)n_hit / n_req << "," << n_req << "," << n_promoted << "\n";
    std::cout << s.str();
    csv_file << s.str();

    reset_reader(reader);
    if (i == 0)
      first_promoted = n_promoted;
    for (auto &e : objs_metadata) {
      e.second.access_counter = 0;
      e.second.last_promotion = 0;
    }
  }

  uint64_t sum = 0;
  for (const auto &e : objs_metadata) {
    sum += e.second.wasted_promotions.size();
  }
  printf("\n\
============\n\
-COMPLETED!-\n\
trace_path: %s\n\
cache_size: %lld\n\
miss_ratio: %f\n\
n_req: %ld\n\
first_promoted: %ld\n\
last_promoted: %ld\n\
iteration: %ld\n\
promotions_reduced: %ld\n\
log: %s\n\
============\n",
         reader->trace_path, cache_size / MiB, 1 - (double)n_hit / n_req, n_req,
         first_promoted, n_promoted, max_iteration, first_promoted - n_promoted,
         log_path.c_str());

  free_request(req);
  cache->cache_free(cache);
  close_reader(reader);
  objs_metadata.clear();
}

struct options {
  std::vector<std::filesystem::path> trace_paths;
  // std::vector<std::string> custom_suffixes;

  std::vector<uint64_t> fixed_cache_sizes;
  std::vector<float> relative_cache_sizes;

  bool ignore_obj_size;
  uint64_t max_iteration;
  std::filesystem::path output_directory;
};

void RunExperiment(const options &o) {
  std::vector<std::future<void>> tasks;
  std::cout << csv_header;

  std::filesystem::create_directories(o.output_directory / "csv");
  std::filesystem::create_directories(o.output_directory / "graph");

  for (const auto &p : o.trace_paths) {
    reader_t *reader = open_trace(p.c_str(), ORACLE_GENERAL_TRACE, NULL);
    reader->ignore_obj_size = o.ignore_obj_size;

    int64_t wss_obj = 0;
    int64_t wss_byte = 0;
    cal_working_set_size(reader, &wss_obj, &wss_byte);

    int64_t wss = o.ignore_obj_size ? wss_obj : wss_byte;

    for (const auto &f : o.fixed_cache_sizes) {
      tasks.emplace_back(std::async(
          std::launch::async, RunClockExperiment, clone_reader(reader),
          o.output_directory / "log", o.output_directory / "datasets", f * MiB,
          std::to_string(f) + "MiB", o.max_iteration));
    }
    for (const auto &r : o.relative_cache_sizes) {
      tasks.emplace_back(std::async(
          std::launch::async, RunClockExperiment, clone_reader(reader),
          o.output_directory / "log", o.output_directory / "datasets", wss * r,
          std::to_string(r), o.max_iteration));
    }
  }

  for (auto &t : tasks) {
    t.get();
  }
}

int main(int argc, char **argv) {
  options o;
  CLI::App app{"Offline Clock Simulator, based on libCacheSim"};
  app.add_option("-f,--fixed-cache-sizes", o.fixed_cache_sizes,
                 "Fixed cache sizes in MiB, can be more than one");
  app.add_option(
      "-r,--relative-cache-sizes", o.relative_cache_sizes,
      "Relative cache sizes in floating number, can be more than one");
  app.add_option("-o,--output-directory", o.output_directory,
                 "Output directory")
      ->default_str("./result");
  app.add_option("--ignore_obj_size", o.ignore_obj_size,
                 "Would ignore object sizes from trace")
      ->default_val(false);
  app.add_option("-i,--max-iteration", o.max_iteration,
                 "Offline clock max iteration")
      ->default_val(10);
  app.add_option("trace_paths", o.trace_paths, "Can be more than one")
      ->required();

  CLI11_PARSE(app, argc, argv);
  RunExperiment(o);
  return 0;
}
