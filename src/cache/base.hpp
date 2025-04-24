#pragma once
#include <libCacheSim/cache.h>

namespace base {
cache_t *BaseClockInit(const common_cache_params_t ccache_params,
                       const char *cache_specific_params);
}
