#include "base.hpp"
#include "common.hpp"

#include <libCacheSim/cache.h>

cache_t *base::BaseClockInit(const common_cache_params_t ccache_params,
                             const char *cache_specific_params) {
  auto cache = Clock_init(ccache_params, cache_specific_params);

  cache->cache_init = BaseClockInit;

  common::Custom_clock_params *params = new common::Custom_clock_params(
      *(Clock_params_t *)cache->eviction_params);
  free(cache->eviction_params);

  cache->eviction_params = params;
  return cache;
}
