#include "base.hpp"
#include <libCacheSim/cache.h>
#include "common.hpp"

static void BaseClockEvict(cache_t* cache, const request_t* req) {
	Clock_params_t* params = (Clock_params_t*)cache->eviction_params;

	cache_obj_t* obj_to_evict = params->q_tail;
	auto custom_params = (common::Custom_clock_params*)params;
	while (obj_to_evict->clock.freq >= 1) {
		common::EvictionTracking(obj_to_evict, custom_params);
		obj_to_evict->clock.freq -= 1;
		params->n_obj_rewritten += 1;
		params->n_byte_rewritten += obj_to_evict->obj_size;
		move_obj_to_head(&params->q_head, &params->q_tail, obj_to_evict);
		obj_to_evict = params->q_tail;
		custom_params->n_promoted++;
	}

	remove_obj_from_list(&params->q_head, &params->q_tail, obj_to_evict);
	cache_evict_base(cache, obj_to_evict, true);
}

cache_t* base::BaseClockInit(
	const common_cache_params_t ccache_params, const char* cache_specific_params
) {
	auto cache = Clock_init(ccache_params, cache_specific_params);

	cache->cache_init = BaseClockInit;
	cache->evict = BaseClockEvict;

	common::Custom_clock_params* params = new common::Custom_clock_params(
		*(Clock_params_t*)cache->eviction_params
	);
	free(cache->eviction_params);

	cache->eviction_params = params;
	return cache;
}
