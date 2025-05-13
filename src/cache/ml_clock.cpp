#include "ml_clock.hpp"
#include "common.hpp"
#include <cmath>
#include <libCacheSim/cache.h>
#include <libCacheSim/evictionAlgo.h>
#include <vector>

template <typename T>
void MLClockEvict(cache_t* cache, const request_t* req) {
	Clock_params_t* params = (Clock_params_t*)cache->eviction_params;
	mlclock::MLClockParam* custom_params = (mlclock::MLClockParam*)cache->eviction_params;

	cache_obj_t* obj_to_evict = params->q_tail;
	while (obj_to_evict->clock.freq >= 1) {
		auto data = custom_params->objs_metadata[obj_to_evict->obj_id];
		std::unordered_map<std::string, T> features;

		float rtime_since = req->clock_time - data.rtime;
		float vtime_since = custom_params->vtime - data.vtime;

		features["rtime_since"] = rtime_since;
		features["rtime_since_log"] = log(rtime_since + 1);
		features["vtime_since"] = vtime_since;
		features["vtime_since_log"] = log(vtime_since + 1);
		features["rtime_between"] = data.rtime_between;
		features["rtime_between_log"] = log(data.rtime_between + 1);
		features["clock_freq"] = data.clock_freq;
		features["clock_freq_log"] = log(data.clock_freq + 1);
		features["clock_freq_norm"] =
			common::RunningMeanNormalize(data.clock_freq, custom_params->mean_clock_freq,
										 custom_params->m2_clock_freq, custom_params->n_clock_freq);
		features["lifetime_freq"] = data.lifetime_freq;
		features["lifetime_freq_log"] = log(data.lifetime_freq + 1);
		features["lifetime_freq_norm"] = common::RunningMeanNormalize(
			data.lifetime_freq, custom_params->mean_lifetime_freq, custom_params->m2_lifetime_freq,
			custom_params->n_lifetime_freq);
		std::vector<T> input_features;
		input_features.reserve(custom_params->features_name.size());
		for (const auto& f : custom_params->features_name) {
			input_features.push_back(features[f]);
		}
		bool wasted = custom_params->PromotionIsWasted(
			input_features, {1, static_cast<long>(input_features.size())});

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

template <typename T>
cache_t* mlclock::MLClockInit(const common_cache_params_t ccache_params,
							  const char* cache_specific_params) {
	auto cache = Clock_init(ccache_params, cache_specific_params);

	cache->cache_init = MLClockInit<T>;
	cache->evict = MLClockEvict<T>;

	MLClockParam* params = new MLClockParam(*(Clock_params_t*)cache->eviction_params);
	free(cache->eviction_params);

	cache->eviction_params = params;
	return cache;
}

template cache* mlclock::MLClockInit<float>(common_cache_params_t, const char*);
template cache* mlclock::MLClockInit<double>(common_cache_params_t, const char*);
template cache* mlclock::MLClockInit<int>(common_cache_params_t, const char*);
template cache* mlclock::MLClockInit<long>(common_cache_params_t, const char*);
