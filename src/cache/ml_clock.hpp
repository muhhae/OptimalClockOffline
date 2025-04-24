#pragma once

#include "cache/common.hpp"
#include <array>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <filesystem>
#include <iostream>
#include <iterator>
#include <libCacheSim/cache.h>
#include <libCacheSim/evictionAlgo.h>
#include <onnxruntime/onnxruntime_c_api.h>
#include <onnxruntime/onnxruntime_cxx_api.h>
#include <optional>
#include <stdexcept>
#include <vector>

namespace mlclock {
cache_t *MLClockInit(const common_cache_params_t ccache_params,
                     const char *cache_specific_params);
class MLClockParam : public common::Custom_clock_params {
public:
  MLClockParam() : env(ORT_LOGGING_LEVEL_WARNING, "ml_clock") {
    session_options.SetIntraOpNumThreads(8);
  }
  MLClockParam(const Clock_params_t &base) : MLClockParam() {
    *(Clock_params_t *)this = base;
  }
  void LoadModel(std::filesystem::path model) {
    try {
      session = Ort::Session(env, model.c_str(), session_options);
    } catch (const Ort::Exception &e) {
      throw std::runtime_error(std::string("Failed to load model: ") +
                               e.what());
    }
  }
  bool PromotionIsWasted(std::vector<int64_t> input,
                         std::array<int64_t, 2> shape) {
    Ort::AllocatorWithDefaultOptions allocator;
    auto input_name = session->GetInputNameAllocated(0, allocator);
    auto output_name = session->GetOutputNameAllocated(0, allocator);

    Ort::MemoryInfo memory_info =
        Ort::MemoryInfo::CreateCpu(OrtDeviceAllocator, OrtMemTypeCPU);

    Ort::Value input_tensor = Ort::Value::CreateTensor<int64_t>(
        memory_info, input.data(), input.size(), shape.data(), shape.size());

    std::array<const char *, 1> input_names = {input_name.get()};
    std::array<const char *, 1> output_names = {output_name.get()};
    auto output_tensors =
        session->Run(Ort::RunOptions{nullptr}, input_names.data(),
                     &input_tensor, 1, output_names.data(), 1);

    int64_t *output_data = output_tensors[0].GetTensorMutableData<int64_t>();
    // std::cout << "Output: " << output_data[0] << std::endl;
    return output_data[0];
  }

public:
  std::optional<Ort::Session> session;
  Ort::Env env;
  Ort::SessionOptions session_options;
};
} // namespace mlclock
