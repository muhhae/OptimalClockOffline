#include "dist_clock.hpp"
#include <libCacheSim/admissionAlgo.h>
#include <libCacheSim/cache.h>
#include <libCacheSim/cacheObj.h>
#include "common.hpp"

static void DistClockEvict(cache_t* cache, const request_t* req) {
	Clock_params_t* params = (Clock_params_t*)cache->eviction_params;
	auto c_params = (common::Custom_clock_params*)params;

	cache_obj_t* obj_to_evict = params->q_tail;
	while (obj_to_evict->clock.freq >= 1) {
		bool wasted = obj_to_evict->obj_id >= c_params->dist_optimal_treshold;
		if (c_params->generate_datasets) {
			auto data = c_params->objs_metadata[obj_to_evict->obj_id];
			auto features = common::CandidateMetadata(data, c_params, cache, req, obj_to_evict);
			features["wasted"] = wasted;
			for (size_t i = 0; i < common::datasets_columns.size(); i++) {
				c_params->datasets << features[common::datasets_columns[i]]
								   << (i == common::datasets_columns.size() - 1 ? '\n' : ',');
			}
		}
		common::BeforeEvictionTracking(obj_to_evict, c_params);
		if (wasted)
			break;
		common::PromotionTracking(obj_to_evict, c_params);
		obj_to_evict->clock.freq -= 1;
		params->n_obj_rewritten += 1;
		params->n_byte_rewritten += obj_to_evict->obj_size;
		move_obj_to_head(&params->q_head, &params->q_tail, obj_to_evict);
		obj_to_evict = params->q_tail;
		c_params->n_promoted++;
	}
	remove_obj_from_list(&params->q_head, &params->q_tail, obj_to_evict);
	cache_evict_base(cache, obj_to_evict, true);
}

cache_t* distclock::DistClockInit(
	const common_cache_params_t ccache_params, const char* cache_specific_params
) {
	auto cache = Clock_init(ccache_params, cache_specific_params);

	cache->cache_init = DistClockInit;
	cache->evict = DistClockEvict;

	common::Custom_clock_params* params =
		new common::Custom_clock_params(*(Clock_params_t*)cache->eviction_params);
	free(cache->eviction_params);
	cache->eviction_params = params;
	return cache;
}
