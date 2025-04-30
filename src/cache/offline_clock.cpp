#include "offline_clock.hpp"

#include <libCacheSim/cache.h>
#include <libCacheSim/evictionAlgo.h>

#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <fstream>

#include "common.hpp"

template <typename T, typename... Args>
void out_dataset(std::ofstream &output, T first, Args... rest) {
  output << first << (sizeof...(rest) > 0 ? "," : "\n");
  if constexpr (sizeof...(rest) > 0) {
    out_dataset(output, rest...);
  }
}

static void OfflineClockEvict(cache_t *cache, const request_t *req) {
  Clock_params_t *params = (Clock_params_t *)cache->eviction_params;
  common::Custom_clock_params *custom_params =
      (common::Custom_clock_params *)cache->eviction_params;

  cache_obj_t *obj_to_evict = params->q_tail;
  while (obj_to_evict->clock.freq >= 1) {
    auto &data = custom_params->objs_metadata[obj_to_evict->obj_id];
    data.last_promotion = data.access_counter;
    bool wasted = data.wasted_promotions.find(data.last_promotion) !=
                  data.wasted_promotions.end();
    if (custom_params->generate_datasets) {
      out_dataset(
          custom_params->datasets, data.current_req_metadata.last_access_rtime,
          data.current_req_metadata.last_access_vtime,
          data.current_req_metadata.create_rtime,
          data.current_req_metadata.clock_time,
          data.current_req_metadata.clock_time_between,
          data.current_req_metadata.compulsory_miss,
          data.current_req_metadata.first_seen, cache->cache_size,
          data.current_req_metadata.obj_size,
          data.current_req_metadata.access_freq, data.access_counter, wasted);
    }
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
  auto &data = custom_params->objs_metadata[obj_to_evict->obj_id];
  data.wasted_promotions.insert(data.last_promotion);
  remove_obj_from_list(&params->q_head, &params->q_tail, obj_to_evict);
  cache_evict_base(cache, obj_to_evict, true);
}

cache_t *cclock::OfflineClockInit(const common_cache_params_t ccache_params,
                                  const char *cache_specific_params) {
  auto custom_clock = Clock_init(ccache_params, cache_specific_params);

  custom_clock->cache_init = OfflineClockInit;
  custom_clock->evict = OfflineClockEvict;

  common::Custom_clock_params *params = new common::Custom_clock_params(
      *(Clock_params_t *)custom_clock->eviction_params);
  free(custom_clock->eviction_params);

  custom_clock->eviction_params = params;
  return custom_clock;
}
