#pragma once

#include <libCacheSim/cache.h>
#include <libCacheSim/reader.h>

#include <filesystem>
#include <string>
#include <vector>

struct options {
  std::string algorithm;
  std::vector<std::filesystem::path> trace_paths;
  // std::vector<std::string> custom_suffixes;

  std::vector<std::string> features_name;
  std::vector<uint64_t> fixed_cache_sizes;
  std::vector<float> relative_cache_sizes;

  bool ignore_obj_size = false;
  bool generate_datasets = false;
  uint64_t max_iteration;
  std::filesystem::path output_directory;
  std::string desc;
  std::string ml_model;
};

void Simulate(cache_t *cache, const std::filesystem::path trace_path,
              const options o, const std::string desc);
void RunExperiment(const options &o);
