#pragma once

#include <cstdint>
#include <fstream>
#include <libCacheSim/cacheObj.h>
#include <libCacheSim/evictionAlgo.h>
#include <libCacheSim/request.h>
#include <sys/types.h>
#include <unordered_map>
#include <unordered_set>

namespace common {

struct obj_metadata {
	uint64_t lifetime_freq = 0;
	uint64_t last_promotion = 0;
	std::unordered_set<uint64_t> wasted_promotions;

	void Track(const request_t* req);
	void Reset();

	int64_t rtime_since = 0;
	int64_t obj_size_relative = 0;
	int64_t clock_freq = 0;
	int64_t rtime_between = 0;
	int64_t rtime = 0;
	int64_t last_access_vtime = 0;
	int64_t last_access_rtime = 0;
	int64_t obj_size = 0;
	int64_t vtime = 0;

	int32_t create_rtime = 0;

	bool first_seen = 0;
	bool compulsory_miss = 0;
};

class Custom_clock_params : public Clock_params_t {
  public:
	Custom_clock_params() = default;
	Custom_clock_params(const Clock_params_t& base) { *(Clock_params_t*)this = base; }
	void GlobalTrack(const obj_metadata& data);

  public:
	std::ofstream datasets;
	std::unordered_map<obj_id_t, obj_metadata> objs_metadata;

	uint64_t n_hit;
	uint64_t n_req;
	uint64_t n_promoted;

	uint64_t max_lifetime_freq = 1;
	uint64_t max_clock_freq = 1;
	uint64_t max_rtime_between = 1;
	uint64_t max_rtime = 1;
	uint64_t max_vtime_since = 1;
	uint64_t max_rtime_since = 1;

	float mean_clock_freq = 0;
	float m2_clock_freq = 0;
	uint64_t clock_freq_count = 0;

	uint64_t vtime = 0;

	bool generate_datasets;
};

static void EvictionTracking(const cache_obj_t* obj, Custom_clock_params* custom_params) {
	auto& data = custom_params->objs_metadata[obj->obj_id];
	data.clock_freq = 0;
}
} // namespace common
