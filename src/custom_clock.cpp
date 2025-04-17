#include "custom_clock.hpp"

#include <cmath>
#include <iostream>
#include <libCacheSim/cache.h>
#include <libCacheSim/evictionAlgo.h>

void CustomClockEvict(cache_t *cache, const request_t *req) {
  Clock_params_t *params = (Clock_params_t *)cache->eviction_params;
  cclock::Custom_clock_params *custom_params =
      (cclock::Custom_clock_params *)cache->eviction_params;
  cache_obj_t *obj_to_evict = params->q_tail;
  while (obj_to_evict->clock.freq >= 1) {
    auto &data = custom_params->objs_metadata[obj_to_evict->obj_id];
    data.last_promotion = data.access_counter;
    if (data.wasted_promotions.find(data.last_promotion) !=
        data.wasted_promotions.end()) {
      break;
    }
    obj_to_evict->clock.freq -= 1;
    params->n_obj_rewritten += 1;
    params->n_byte_rewritten += obj_to_evict->obj_size;
    move_obj_to_head(&params->q_head, &params->q_tail, obj_to_evict);
    custom_params->n_promoted++;
    obj_to_evict = params->q_tail;
  }
  auto &data = custom_params->objs_metadata[obj_to_evict->obj_id];
  data.wasted_promotions.insert(data.last_promotion);
  remove_obj_from_list(&params->q_head, &params->q_tail, obj_to_evict);
  cache_evict_base(cache, obj_to_evict, true);
}

cache_t *cclock::CustomClockInit(const common_cache_params_t ccache_params,
                                 const char *cache_specific_params) {
  auto custom_clock = Clock_init(ccache_params, cache_specific_params);
  custom_clock->evict = CustomClockEvict;
  custom_clock->cache_init = CustomClockInit;

  Custom_clock_params *params =
      new Custom_clock_params(*(Clock_params_t *)custom_clock->eviction_params);
  free(custom_clock->eviction_params);

  custom_clock->eviction_params = params;
  return custom_clock;
}
