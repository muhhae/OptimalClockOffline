#include "custom_clock.hpp"

#include <libCacheSim/cache.h>
#include <libCacheSim/evictionAlgo.h>

#include "obj_metadata.hpp"

void CustomClockEvict(cache_t *cache, const request_t *req) {
  Clock_params_t *params = (Clock_params_t *)cache->eviction_params;
  cache_obj_t *obj_to_evict = params->q_tail;
  while (obj_to_evict->clock.freq >= 1) {
    auto &data = objs_metadata[obj_to_evict->obj_id];
    if (data.wasted_promotions.find(data.access_counter) !=
        data.wasted_promotions.end()) {
      break;
    }
    data.last_promotion = data.access_counter;
    obj_to_evict->clock.freq -= 1;
    params->n_obj_rewritten += 1;
    params->n_byte_rewritten += obj_to_evict->obj_size;
    move_obj_to_head(&params->q_head, &params->q_tail, obj_to_evict);
    n_promoted++;
    obj_to_evict = params->q_tail;
  }
  auto &data = objs_metadata[obj_to_evict->obj_id];
  data.wasted_promotions.insert(data.last_promotion);
  remove_obj_from_list(&params->q_head, &params->q_tail, obj_to_evict);
  cache_evict_base(cache, obj_to_evict, true);
}

cache_t *cclock::CustomClockInit(const common_cache_params_t ccache_params,
                                 const char *cache_specific_params) {
  auto custom_clock = Clock_init(ccache_params, cache_specific_params);
  custom_clock->evict = CustomClockEvict;
  custom_clock->cache_init = CustomClockInit;
  return custom_clock;
}
