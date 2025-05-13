#include "offline_clock.hpp"
#include "common.hpp"
#include <cmath>
#include <cstdlib>
#include <fstream>
#include <libCacheSim/cache.h>
#include <libCacheSim/evictionAlgo.h>

template <typename T, typename... Args>
void out_dataset(std::ofstream& output, T first, Args... rest) {
	output << first << (sizeof...(rest) > 0 ? "," : "\n");
	if constexpr (sizeof...(rest) > 0) {
		out_dataset(output, rest...);
	}
}

static void OfflineClockEvict(cache_t* cache, const request_t* req) {
	Clock_params_t* params = (Clock_params_t*)cache->eviction_params;
	common::Custom_clock_params* custom_params =
		(common::Custom_clock_params*)cache->eviction_params;

	cache_obj_t* obj_to_evict = params->q_tail;
	while (obj_to_evict->clock.freq >= 1) {
		auto& data = custom_params->objs_metadata[obj_to_evict->obj_id];
		data.last_promotion = data.lifetime_freq;
		bool wasted =
			data.wasted_promotions.find(data.last_promotion) != data.wasted_promotions.end();
		if (custom_params->generate_datasets) {
			float rtime_since = req->clock_time - data.rtime;
			float vtime_since = custom_params->vtime - data.vtime;

			custom_params->datasets << obj_to_evict->obj_id << ",";
			custom_params->datasets << rtime_since << ",";
			custom_params->datasets << log(rtime_since + 1) << ",";
			custom_params->datasets << vtime_since << ",";
			custom_params->datasets << log(vtime_since + 1) << ",";
			custom_params->datasets << data.rtime_between << ",";
			custom_params->datasets << log(data.rtime_between + 1) << ",";
			custom_params->datasets << data.clock_freq << ",";
			custom_params->datasets << log(data.clock_freq + 1) << ",";

			custom_params->datasets
				<< common::RunningMeanNormalize(data.clock_freq, custom_params->mean_clock_freq,
												custom_params->m2_clock_freq,
												custom_params->n_clock_freq)
				<< ",";

			custom_params->datasets << data.lifetime_freq << ",";
			custom_params->datasets << log(data.lifetime_freq + 1) << ",";

			custom_params->datasets
				<< common::RunningMeanNormalize(
					   data.lifetime_freq, custom_params->mean_lifetime_freq,
					   custom_params->m2_lifetime_freq, custom_params->n_lifetime_freq)
				<< ",";

			custom_params->datasets << wasted << "\n";
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
	auto& data = custom_params->objs_metadata[obj_to_evict->obj_id];
	data.wasted_promotions.insert(data.last_promotion);
	remove_obj_from_list(&params->q_head, &params->q_tail, obj_to_evict);
	cache_evict_base(cache, obj_to_evict, true);
}

cache_t* cclock::OfflineClockInit(const common_cache_params_t ccache_params,
								  const char* cache_specific_params) {
	auto custom_clock = Clock_init(ccache_params, cache_specific_params);

	custom_clock->cache_init = OfflineClockInit;
	custom_clock->evict = OfflineClockEvict;

	common::Custom_clock_params* params =
		new common::Custom_clock_params(*(Clock_params_t*)custom_clock->eviction_params);
	free(custom_clock->eviction_params);

	custom_clock->eviction_params = params;
	return custom_clock;
}
