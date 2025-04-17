#pragma once

#include <libCacheSim/cache.h>
#include <libCacheSim/evictionAlgo.h>
#include <string>
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
  std::unordered_map<obj_id_t, obj_metadata> objs_metadata;

  uint64_t n_hit;
  uint64_t n_req;
  uint64_t n_promoted;

  bool generate_datasets;
};

cache_t *CustomClockInit(const common_cache_params_t ccache_params,
                         const char *cache_specific_params);
} // namespace cclock
