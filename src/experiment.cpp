#include "experiment.hpp"
#include "custom_clock.hpp"
#include "lib/cache_size.h"
#include "obj_metadata.hpp"

#include <cstdint>
#include <fstream>
#include <functional>
#include <future>
#include <iostream>
#include <stdexcept>

const std::string csv_header =
    "trace_path,ignore_obj_size,cache_size,miss_ratio,n_req,n_promoted\n";

void Simulate(cache_t *cache, const std::filesystem::path trace_path,
              const std::filesystem::path log_dir,
              const std::filesystem::path datasets_dir,
              const bool ignore_obj_size, const std::string output_suffix,
              const uint64_t max_iteration) {
  reader_init_param_t param = default_reader_init_params();
  param.ignore_obj_size = ignore_obj_size;

  reader_t *reader =
      open_trace(trace_path.c_str(), ORACLE_GENERAL_TRACE, &param);

  request_t *req = new_request();

  std::string base_path = std::filesystem::path(reader->trace_path).filename();
  size_t pos = base_path.find(".oracleGeneral");
  if (pos != std::string::npos) {
    base_path = base_path.substr(0, pos);
  }
  std::filesystem::path log_path =
      log_dir / (base_path + output_suffix + ".csv");
  std::filesystem::path dataset_path =
      datasets_dir / (base_path + output_suffix + ".csv");

  std::ofstream csv_file(log_path);
  csv_file << csv_header;

  std::ofstream dataset(dataset_path);
  dataset << "";

  printf("\n\
============\n\
---start!---\n\
trace_path: %s\n\
cache_size: %lld\n\
ignore_obj_size: %d\n\
iteration: %ld\n\
log: %s\n\
============\n",
         reader->trace_path,
         reader->ignore_obj_size ? cache->cache_size : cache->cache_size / MiB,
         reader->ignore_obj_size, max_iteration, log_path.c_str());

  uint64_t first_promoted = 0;

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

    std::ostringstream s;
    s << std::filesystem::path(reader->trace_path).filename() << ","
      << reader->ignore_obj_size << ","
      << (reader->ignore_obj_size ? cache->cache_size : cache->cache_size / MiB)
      << "," << 1 - (double)n_hit / n_req << "," << n_req << "," << n_promoted
      << "\n";
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
ignore_obj_size: %d\n\
miss_ratio: %f\n\
n_req: %ld\n\
first_promoted: %ld\n\
last_promoted: %ld\n\
iteration: %ld\n\
promotions_reduced: %ld\n\
log: %s\n\
============\n",
         reader->trace_path,
         reader->ignore_obj_size ? cache->cache_size : cache->cache_size / MiB,
         reader->ignore_obj_size, 1 - (double)n_hit / n_req, n_req,
         first_promoted, n_promoted, max_iteration, first_promoted - n_promoted,
         log_path.c_str());

  free_request(req);
  cache->cache_free(cache);
  close_reader(reader);
  objs_metadata.clear();
}

void RunExperiment(const options &o) {
  std::vector<std::future<void>> tasks;
  std::function<cache_t *(const common_cache_params_t ccache_params,
                          const char *cache_specific_params)>
      CacheInit;
  if (o.algorithm == "default") {
    CacheInit = cclock::CustomClockInit;
  } else if (o.algorithm == "bob") {
    throw std::runtime_error("bob's algorithm hasn't been implemented");
  } else {
    throw std::runtime_error("algorithm not found");
  }

  std::filesystem::create_directories(o.output_directory / "log");
  std::filesystem::create_directories(o.output_directory / "datasets");

  for (const auto &p : o.trace_paths) {
    reader_init_param_t reader_init_param = {.ignore_obj_size =
                                                 o.ignore_obj_size};
    reader_t *reader =
        open_trace(p.c_str(), ORACLE_GENERAL_TRACE, &reader_init_param);

    int64_t wss_obj = 0;
    int64_t wss_byte = 0;
    if (!o.relative_cache_sizes.empty())
      cal_working_set_size(reader, &wss_obj, &wss_byte);

    close_reader(reader);
    int64_t wss = o.ignore_obj_size ? wss_obj : wss_byte;

    std::cout << csv_header;
    for (const auto &fcs : o.fixed_cache_sizes) {
      std::string desc = "[" + std::to_string(fcs) +
                         (o.ignore_obj_size ? "" : "MiB") +
                         (o.desc != "" ? "," : "") + o.desc + "]";
      tasks.emplace_back(std::async(
          std::launch::async, Simulate,
          cclock::CustomClockInit(
              {.cache_size = o.ignore_obj_size ? fcs : fcs * MiB}, NULL),
          p, o.output_directory / "log", o.output_directory / "datasets",
          o.ignore_obj_size, desc, o.max_iteration));
    }
    for (const auto &rcs : o.relative_cache_sizes) {
      std::string s = std::to_string(rcs);
      s = s.substr(0, s.find_last_not_of('0') + 1);
      if (s.back() == '.')
        s.pop_back();

      std::string desc = "[" + s + (o.desc != "" ? "," : "") + o.desc + "]";
      tasks.emplace_back(std::async(
          std::launch::async, Simulate,
          cclock::CustomClockInit({.cache_size = uint64_t(wss * rcs)}, NULL), p,
          o.output_directory / "log", o.output_directory / "datasets",
          o.ignore_obj_size, desc, o.max_iteration));
    }
  }

  for (auto &t : tasks) {
    t.get();
  }
}
