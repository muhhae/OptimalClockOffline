#include "experiment.hpp"
#include "cache/base.hpp"
#include "cache/common.hpp"
#include "cache/ml_clock.hpp"
#include "cache/my_clock.hpp"
#include "cache/offline_clock.hpp"
#include "lib/cache_size.h"

#include <algorithm>
#include <cstddef>
#include <cstdint>
#include <cstdio>
#include <fstream>
#include <functional>
#include <future>
#include <iostream>
#include <libCacheSim/cache.h>
#include <stdexcept>
#include <string>

const std::string csv_header =
    "trace_path,ignore_obj_size,cache_size,miss_ratio,n_req,n_promoted\n";

void RunExperiment(const options &o) {
  std::vector<std::future<void>> tasks;
  std::function<cache_t *(const common_cache_params_t ccache_params,
                          const char *cache_specific_params)>
      CacheInit;
  if (o.algorithm == "default") {
    CacheInit = cclock::OfflineClockInit;
  } else if (o.algorithm == "base") {
    CacheInit = base::BaseClockInit;
  } else if (o.algorithm == "my") {
    CacheInit = myclock::MyClockInit;
  } else if (o.algorithm == "ML") {
    CacheInit = mlclock::MLClockInit;
    if (o.ml_model == "") {
      throw std::runtime_error("ML model need to be provided in ONNX format");
    }
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

    const char *cache_specific_params = NULL;

    std::cout << csv_header;
    for (const auto &fcs : o.fixed_cache_sizes) {
      std::string desc = "[" + std::to_string(fcs) +
                         (o.ignore_obj_size ? "" : "MiB") +
                         (o.desc != "" ? "," : "") + o.desc + "]";
      tasks.emplace_back(std::async(
          std::launch::async, Simulate,
          CacheInit({.cache_size = o.ignore_obj_size ? fcs : fcs * MiB},
                    cache_specific_params),
          p, o, desc));
    }
    for (const auto &rcs : o.relative_cache_sizes) {
      std::string s = std::to_string(rcs);
      s = s.substr(0, s.find_last_not_of('0') + 1);
      if (s.back() == '.')
        s.pop_back();

      std::string desc = "[" + s + (o.desc != "" ? "," : "") + o.desc + "]";
      tasks.emplace_back(std::async(
          std::launch::async, Simulate,
          CacheInit({.cache_size = uint64_t(wss * rcs)}, cache_specific_params),
          p, o, desc));
    }
  }

  for (auto &t : tasks) {
    t.get();
  }
}

void Simulate(cache_t *cache, const std::filesystem::path trace_path,
              const options o, const std::string desc) {
  reader_init_param_t param = default_reader_init_params();
  param.ignore_obj_size = o.ignore_obj_size;

  reader_t *reader =
      open_trace(trace_path.c_str(), ORACLE_GENERAL_TRACE, &param);

  request_t *req = new_request();

  std::string base_path = std::filesystem::path(reader->trace_path).filename();
  size_t pos = base_path.find(".oracleGeneral");
  if (pos != std::string::npos) {
    base_path = base_path.substr(0, pos);
  }
  std::filesystem::path log_path =
      o.output_directory / "log" / (base_path + desc + ".csv");
  std::filesystem::path dataset_path =
      o.output_directory / "datasets" / (base_path + desc + ".csv");

  std::ofstream csv_file(log_path);
  csv_file << csv_header;

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
         reader->ignore_obj_size, o.max_iteration, log_path.c_str());

  uint64_t first_promoted = 0;
  common_cache_params_t *params =
      (common_cache_params_t *)cache->eviction_params;

  common::Custom_clock_params *custom_params =
      (common::Custom_clock_params *)cache->eviction_params;

  custom_params->datasets = std::ofstream(dataset_path);
  custom_params->datasets
      << "last_access_rtime, "
         "last_access_vtime, create_rtime, clock_time, clock_time_between, "
         "compulsory_miss, "
         "first_seen, cache_size, obj_size, clock_freq, lifetime_freq, "
         "wasted\n";

  for (size_t i = 0; i < o.max_iteration; ++i) {
    auto tmp = clone_cache(cache);
    auto tmp_custom_params =
        (common::Custom_clock_params *)tmp->eviction_params;
    std::swap(tmp_custom_params->objs_metadata, custom_params->objs_metadata);
    std::swap(tmp_custom_params->datasets, custom_params->datasets);
    std::swap(tmp_custom_params->n_hit, custom_params->n_hit);
    std::swap(tmp_custom_params->n_req, custom_params->n_req);
    std::swap(tmp_custom_params->n_promoted, custom_params->n_promoted);

    tmp_custom_params->n_hit = 0;
    tmp_custom_params->n_req = 0;
    tmp_custom_params->n_promoted = 0;
    if (i == o.max_iteration - 1) {
      tmp_custom_params->generate_datasets = o.generate_datasets;
    }
    while (read_one_req(reader, req) == 0) {
      auto &data = tmp_custom_params->objs_metadata[req->obj_id];
      data.access_counter += 1;
      data.current_req_metadata.Track(req);
      if (tmp->get(tmp, req)) {
        tmp_custom_params->n_hit++;
      }
      tmp_custom_params->n_req++;
    }

    std::ostringstream s;
    s << std::filesystem::path(reader->trace_path).filename() << ","
      << reader->ignore_obj_size << ","
      << (reader->ignore_obj_size ? cache->cache_size : cache->cache_size / MiB)
      << "," << 1 - (double)tmp_custom_params->n_hit / tmp_custom_params->n_req
      << "," << tmp_custom_params->n_req << "," << tmp_custom_params->n_promoted
      << "\n";
    std::cout << s.str();
    csv_file << s.str();

    reset_reader(reader);
    if (i == 0)
      first_promoted = tmp_custom_params->n_promoted;
    for (auto &e : tmp_custom_params->objs_metadata) {
      e.second.access_counter = 0;
      e.second.last_promotion = 0;
      e.second.current_req_metadata = {};
    }
    std::swap(tmp_custom_params->objs_metadata, custom_params->objs_metadata);
    std::swap(tmp_custom_params->datasets, custom_params->datasets);
    std::swap(tmp_custom_params->n_hit, custom_params->n_hit);
    std::swap(tmp_custom_params->n_req, custom_params->n_req);
    std::swap(tmp_custom_params->n_promoted, custom_params->n_promoted);

    tmp->cache_free(tmp);
  }

  custom_params->datasets.close();
  csv_file.close();

  uint64_t sum = 0;
  for (const auto &e : custom_params->objs_metadata) {
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
         reader->ignore_obj_size,
         1 - (double)custom_params->n_hit / custom_params->n_req,
         custom_params->n_req, first_promoted, custom_params->n_promoted,
         o.max_iteration, first_promoted - custom_params->n_promoted,
         log_path.c_str());

  custom_params->objs_metadata.clear();
  free_request(req);
  cache->cache_free(cache);
  close_reader(reader);
}
