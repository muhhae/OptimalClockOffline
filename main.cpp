#include <algorithm>
#include <cstdlib>
#include <cstring>
#include <filesystem>
#include <fstream>
#include <future>
#include <libCacheSim/cache.h>
#include <libCacheSim/const.h>
#include <matplot/core/figure_registry.h>
#include <matplot/freestanding/axes_functions.h>
#include <matplot/freestanding/axes_lim.h>
#include <matplot/freestanding/plot.h>
#include <matplot/matplot.h>
#include <matplot/util/common.h>

#include <cmath>
#include <cstddef>
#include <cstdint>
#include <cstdio>
#include <matplot/util/keywords.h>
#include <sstream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

#include "libCacheSim.h"

std::string output_dir = "";

const std::string csv_header =
    "trace_path,cache_size(MiB),miss_ratio,n_req,n_promoted\n";

struct obj_metadata {
  uint64_t access_counter = 0;
  uint64_t last_promotion = 0;
  std::unordered_set<uint64_t> wasted_promotions;
};

thread_local int64_t n_hit = 0;
thread_local int64_t n_req = 0;
thread_local int64_t n_promoted = 0;
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

void RunClockExperiment(std::string trace_path, const trace_type_e trace_type,
                        const uint64_t cache_size,
                        const uint64_t MAX_ITERATION) {
  reader_t *reader = open_trace(trace_path.c_str(), trace_type, NULL);
  request_t *req = new_request();
  cache_t *cache = Clock_init({.cache_size = cache_size}, NULL);
  cache->evict = clock_custom_evict;

  std::string base_path = "/" + std::filesystem::path(trace_path).string();
  size_t pos = base_path.find(".oracleGeneral");
  if (pos != std::string::npos) {
    base_path = base_path.substr(0, pos);
  }
  base_path += "_" + std::to_string(cache_size / MiB) + "MiB";
  std::string log_path = output_dir + "/log" + base_path + ".csv";
  std::string graph_path = output_dir + "/graph" + base_path + ".png";
  std::ofstream log_file(log_path);
  log_file << csv_header;

  printf("\n\
============\n\
---start!---\n\
trace_path: %s\n\
cache_size: %lld\n\
iteration: %ld\n\
log: %s\n\
graph: %s\n\
============\n",
         trace_path.c_str(), cache_size / MiB, MAX_ITERATION, log_path.c_str(),
         graph_path.c_str());

  uint64_t first_promoted = 0;
  std::vector<uint64_t> promotions;
  std::vector<double> miss_ratios;

  for (size_t i = 0; i < MAX_ITERATION; ++i) {
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
    s << "\"" << trace_path << "\"," << cache_size / MiB << ","
      << 1 - (double)n_hit / n_req << "," << n_req << "," << n_promoted << "\n";
    std::cout << s.str();
    log_file << s.str();

    reset_reader(reader);
    if (i == 0)
      first_promoted = n_promoted;
    for (auto &e : objs_metadata) {
      e.second.access_counter = 0;
      e.second.last_promotion = 0;
    }
  }

  std::string title = std::filesystem::path(graph_path).stem().string();
  std::replace(title.begin(), title.end(), '_', ' ');

  auto iteration = matplot::linspace(0, MAX_ITERATION, 10);
  auto f = matplot::figure(true);
  f->title(title);
  auto ax = f->add_axes();

  auto plt_pm = ax->plot(iteration, promotions);
  matplot::hold(matplot::on);
  auto plt_mr = ax->plot(iteration, miss_ratios)->use_y2(true);

  ax->x_axis().label("Iteration");
  ax->y2_axis().label("Miss Ratio").limits({0, 1});
  ax->y_axis().label("Promotions");

  f->save(graph_path);

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
graph: %s\n\
============\n",
         trace_path.c_str(), cache_size / MiB, 1 - (double)n_hit / n_req, n_req,
         first_promoted, n_promoted, MAX_ITERATION, first_promoted - n_promoted,
         log_path.c_str(), graph_path.c_str());

  free_request(req);
  cache->cache_free(cache);
  close_reader(reader);
  objs_metadata.clear();
}

int main(int argc, char **argv) {
  std::vector<std::future<void>> tasks;
  if (argc < 3) {
    std::cout << "usage: cacheSimulator <out_dir> <trace_dir>\n";
    std::exit(1);
  }
  output_dir = argv[1];
  std::cout << csv_header;
  std::filesystem::create_directories(output_dir + "/log");
  std::filesystem::create_directories(output_dir + "/graph");
  for (size_t i = 2; i < argc; i++) {
    std::filesystem::path p(argv[i]);
    for (size_t i = 0; i < 5; i++) {
      tasks.emplace_back(std::async(std::launch::async, RunClockExperiment,
                                    p.string(), ORACLE_GENERAL_TRACE,
                                    128 * std::pow(2, i) * MiB, 20));
    }
  }
  for (auto &t : tasks) {
    t.get();
  }
  return 0;
}
