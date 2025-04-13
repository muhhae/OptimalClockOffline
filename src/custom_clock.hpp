#pragma once

#include <libCacheSim/cache.h>
#include <libCacheSim/evictionAlgo.h>

namespace cclock {
cache_t *CustomClockInit(const common_cache_params_t ccache_params,
                         const char *cache_specific_params);
}
