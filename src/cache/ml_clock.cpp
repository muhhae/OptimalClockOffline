#include "ml_clock.hpp"
#include "common.hpp"

#include <cmath>
#include <cstdint>
#include <cstdio>
#include <libCacheSim/cache.h>
#include <libCacheSim/evictionAlgo.h>

void MLClockEvict(cache_t *cache, const request_t *req) {
  Clock_params_t *params = (Clock_params_t *)cache->eviction_params;
  mlclock::MLClockParam *custom_params =
      (mlclock::MLClockParam *)cache->eviction_params;

  cache_obj_t *obj_to_evict = params->q_tail;
  while (obj_to_evict->clock.freq >= 1) {
    auto data = custom_params->objs_metadata[obj_to_evict->obj_id];
    int64_t clock_time = data.current_req_metadata.clock_time;
    int64_t clock_time_between = data.current_req_metadata.clock_time_between;
    int64_t cache_size = cache->cache_size;
    int64_t obj_size = obj_to_evict->obj_size;
    int64_t lifetime_freq = data.access_counter;
    int64_t clock_freq = data.current_req_metadata.access_freq;
    bool wasted = custom_params->PromotionIsWasted(
        {clock_time, clock_time_between, cache_size, obj_size, clock_freq,
         lifetime_freq},
        {1, 6});

    common::EvictionTracking(obj_to_evict, custom_params);
    if (wasted) {
      break;
    }
    obj_to_evict->clock.freq -= 1;
    params->n_obj_rewritten += 1;
    params->n_byte_rewritten += obj_to_evict->obj_size;
    move_obj_to_head(&params->q_head, &params->q_tail, obj_to_evict);
    custom_params->n_promoted++;
    obj_to_evict = params->q_tail;
  }
  remove_obj_from_list(&params->q_head, &params->q_tail, obj_to_evict);
  cache_evict_base(cache, obj_to_evict, true);
}

cache_t *mlclock::MLClockInit(const common_cache_params_t ccache_params,
                              const char *cache_specific_params) {
  auto cache = Clock_init(ccache_params, cache_specific_params);

  cache->cache_init = MLClockInit;
  cache->evict = MLClockEvict;

  MLClockParam *params =
      new MLClockParam(*(Clock_params_t *)cache->eviction_params);
  free(cache->eviction_params);

  cache->eviction_params = params;
  return cache;
}
