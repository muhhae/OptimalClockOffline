#pragma once

#include <libCacheSim/cache.h>
#include <libCacheSim/reader.h>

#include <filesystem>
#include <vector>

const std::string csv_header =
    "trace_path,cache_size(MiB),miss_ratio,n_req,n_promoted\n";

void Simulate(cache_t *cache, const std::filesystem::path trace_path,
              const std::filesystem::path log_dir,
              const std::filesystem::path datasets_dir,
              const bool ignore_obj_size, const std::string output_suffix,
              const uint64_t max_iteration = 10);

struct options {
  std::vector<std::filesystem::path> trace_paths;
  // std::vector<std::string> custom_suffixes;

  std::vector<uint64_t> fixed_cache_sizes;
  std::vector<float> relative_cache_sizes;

  bool ignore_obj_size;
  uint64_t max_iteration;
  std::filesystem::path output_directory;
  std::string desc;
};

void RunExperiment(const options &o);
