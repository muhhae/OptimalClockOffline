#pragma once

#include <libCacheSim/cacheObj.h>
#include <libCacheSim/evictionAlgo.h>
#include <libCacheSim/request.h>
#include <sys/types.h>
#include <cstdint>
#include <fstream>
#include <limits>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

namespace common {

const static std::vector<std::string> datasets_columns = {
	"obj_id",
	"rtime_since",
	"rtime_since_log",
	"rtime_since_std",
	"rtime_since_log_std",
	"vtime_since",
	"vtime_since_log",
	"vtime_since_std",
	"vtime_since_log_std",
	"rtime_between",
	"rtime_between_log",
	"rtime_between_std",
	"rtime_between_log_std",
	"clock_freq",
	"clock_freq_log",
	"clock_freq_std",
	"clock_freq_log_std",
	"lifetime_freq",
	"lifetime_freq_log",
	"lifetime_freq_std",
	"lifetime_freq_log_std",
	"wasted"
};

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

struct RunningMeanData {
	float mean = 0;
	float m2 = 0;
	uint64_t n = 0;
};

class Custom_clock_params : public Clock_params_t {
   public:
	Custom_clock_params() = default;
	Custom_clock_params(const Clock_params_t& base) {
		*(Clock_params_t*)this = base;
	}
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

	RunningMeanData rm_clock_freq;
	RunningMeanData rm_lifetime_freq;
	RunningMeanData rm_vtime_since;
	RunningMeanData rm_rtime_since;
	RunningMeanData rm_rtime_between;

	RunningMeanData rm_clock_freq_log;
	RunningMeanData rm_lifetime_freq_log;
	RunningMeanData rm_vtime_since_log;
	RunningMeanData rm_rtime_since_log;
	RunningMeanData rm_rtime_between_log;

	uint64_t vtime = 0;

	uint64_t dist_optimal_treshold = std::numeric_limits<uint64_t>::max();
	bool generate_datasets;
};

static void BeforeEvictionTracking(const cache_obj_t* obj, Custom_clock_params* custom_params) {
	auto& data = custom_params->objs_metadata[obj->obj_id];
	data.clock_freq = 0;
}

static void PromotionTracking(const cache_obj_t* obj, Custom_clock_params* custom_params) {
	auto& data = custom_params->objs_metadata[obj->obj_id];
	// data.Reset();
}

std::unordered_map<std::string, float> CandidateMetadata(
	const common::obj_metadata& data, common::Custom_clock_params* params,
	const request_t* current_req
);

void TrackRunningMean(const float X, RunningMeanData& d);
float RunningMeanNormalize(const float X, RunningMeanData& d);
}  // namespace common
