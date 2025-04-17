#include "my_clock.hpp"

#include <cmath>
#include <cstdint>
#include <cstdio>
#include <libCacheSim/cache.h>
#include <libCacheSim/evictionAlgo.h>

void MyClockEvict(cache_t *cache, const request_t *req) {
  Clock_params_t *params = (Clock_params_t *)cache->eviction_params;
  myclock::Custom_clock_params *custom_params =
      (myclock::Custom_clock_params *)cache->eviction_params;

  cache_obj_t *obj_to_evict = params->q_tail;
  while (obj_to_evict->clock.freq >= 1) {
    auto &data = custom_params->objs_metadata[obj_to_evict->obj_id];
    uint64_t second_to_last_promotion = data.last_promotion;
    data.last_promotion = data.access_counter;
    uint64_t gap_between_last_promotion =
        data.last_promotion - second_to_last_promotion;
    if (gap_between_last_promotion != 0 && gap_between_last_promotion < 4) {
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

cache_t *myclock::MyClockInit(const common_cache_params_t ccache_params,
                              const char *cache_specific_params) {
  auto my_clock = Clock_init(ccache_params, cache_specific_params);

  my_clock->cache_init = MyClockInit;
  my_clock->evict = MyClockEvict;

  Custom_clock_params *params =
      new Custom_clock_params(*(Clock_params_t *)my_clock->eviction_params);
  free(my_clock->eviction_params);

  my_clock->eviction_params = params;
  return my_clock;
}
