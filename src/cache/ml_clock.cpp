#include "ml_clock.hpp"
#include "common.hpp"
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

		features["rtime"] = data.rtime;
		features["time_since"] = data.rtime_since;
		features["rtime_between"] = data.rtime_between;
		features["cache_size"] = cache->cache_size;
		features["obj_size"] = obj_to_evict->obj_size;
		features["obj_size_relative"] = obj_to_evict->obj_size * 1e6 / cache->cache_size;
		features["lifetime_freq"] = data.lifetime_freq;
		features["clock_freq"] = data.clock_freq;
		features["rtime_between_norm"] =
			(float)data.rtime_between / custom_params->max_rtime_between;
		features["clock_freq_norm"] = (float)data.clock_freq / custom_params->max_clock_freq;
		features["lifetime_freq_norm"] =
			(float)data.lifetime_freq / custom_params->max_lifetime_freq;
		features["rtime_since"] = req->clock_time - data.rtime;
		features["vtime_since"] = custom_params->vtime - data.vtime;

		if (features["rtime_since"] > custom_params->max_rtime_since)
			custom_params->max_rtime_since = features["rtime_since"];
		if (features["vtime_since"] > custom_params->max_vtime_since)
			custom_params->max_vtime_since = features["vtime_since"];

		features["rtime_since_norm"] = features["rtime_since"] / custom_params->max_rtime_since;
		features["vtime_since_norm"] = features["vtime_since"] / custom_params->max_vtime_since;

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
