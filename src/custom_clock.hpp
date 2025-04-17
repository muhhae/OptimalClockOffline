#pragma once

#include <fstream>
#include <libCacheSim/cache.h>
#include <libCacheSim/evictionAlgo.h>
#include <unordered_map>
#include <unordered_set>

namespace cclock {
struct obj_metadata {
  uint64_t access_counter = 0;
  uint64_t last_promotion = 0;
  std::unordered_set<uint64_t> wasted_promotions;
};

class Custom_clock_params : public Clock_params_t {
public:
  Custom_clock_params() = default;
  Custom_clock_params(const Clock_params_t &base) {
    *(Clock_params_t *)this = base;
  }

public:
  std::ofstream datasets;
  std::unordered_map<obj_id_t, obj_metadata> objs_metadata;

  uint64_t n_hit;
  uint64_t n_req;
  uint64_t n_promoted;

  bool generate_datasets;
};

cache_t *CustomClockInit(const common_cache_params_t ccache_params,
                         const char *cache_specific_params);
} // namespace cclock
