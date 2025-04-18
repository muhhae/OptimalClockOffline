#pragma once

#include <libCacheSim/cache.h>
#include <libCacheSim/reader.h>

#include <filesystem>
#include <vector>

void Simulate(cache_t *cache, const std::filesystem::path trace_path,
              const std::filesystem::path log_dir,
              const std::filesystem::path datasets_dir,
              const bool ignore_obj_size, const std::string output_suffix,
              const uint64_t max_iteration, bool generate_datasets);

struct options {
  std::string algorithm;
  std::vector<std::filesystem::path> trace_paths;
  // std::vector<std::string> custom_suffixes;

  std::vector<uint64_t> fixed_cache_sizes;
  std::vector<float> relative_cache_sizes;

  bool ignore_obj_size = false;
  bool generate_datasets = false;
  uint64_t max_iteration;
  std::filesystem::path output_directory;
  std::string desc;
};

void RunExperiment(const options &o);
