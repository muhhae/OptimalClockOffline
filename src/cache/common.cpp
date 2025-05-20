#include "common.hpp"
#include <libCacheSim/reader.h>
#include <sys/types.h>
#include <cmath>
#include <unordered_map>

std::unordered_map<std::string, float> common::CandidateMetadata(
	const common::obj_metadata& data, common::Custom_clock_params* params,
	const request_t* current_req
) {
	float rtime_since = current_req->clock_time - data.rtime;
	float vtime_since = params->vtime - data.vtime;

	TrackRunningMean(rtime_since, params->rm_rtime_since);
	TrackRunningMean(log(rtime_since + 1), params->rm_rtime_since_log);

	TrackRunningMean(vtime_since, params->rm_vtime_since);
	TrackRunningMean(log(vtime_since + 1), params->rm_vtime_since_log);

	std::unordered_map<std::string, float> features;
	features["rtime_since"] = rtime_since;
	features["rtime_since_std"] = common::RunningMeanNormalize(rtime_since, params->rm_rtime_since);
	features["rtime_since_log"] = log(rtime_since + 1);
	features["rtime_since_log_std"] = common::RunningMeanNormalize(
		log(rtime_since + 1), params->rm_rtime_since_log
	);

	features["vtime_since"] = vtime_since;
	features["vtime_since_std"] = common::RunningMeanNormalize(vtime_since, params->rm_vtime_since);
	features["vtime_since_log"] = log(vtime_since + 1);
	features["vtime_since_log_std"] = common::RunningMeanNormalize(
		log(vtime_since + 1), params->rm_vtime_since_log
	);

	features["rtime_between"] = data.rtime_between;
	features["rtime_between_std"] = common::RunningMeanNormalize(
		data.rtime_between, params->rm_rtime_between
	);
	features["rtime_between_log"] = log(data.rtime_between + 1);
	features["rtime_between_log_std"] = common::RunningMeanNormalize(
		log(data.rtime_between + 1), params->rm_rtime_between_log
	);

	features["clock_freq"] = data.clock_freq;
	features["clock_freq_std"] = common::RunningMeanNormalize(
		data.clock_freq, params->rm_clock_freq
	);
	features["clock_freq_log"] = log(data.clock_freq + 1);
	features["clock_freq_log_std"] = common::RunningMeanNormalize(
		log(data.clock_freq + 1), params->rm_clock_freq_log
	);

	features["lifetime_freq"] = data.lifetime_freq;
	features["lifetime_freq_std"] = common::RunningMeanNormalize(
		data.lifetime_freq, params->rm_lifetime_freq
	);
	features["lifetime_freq_log"] = log(data.lifetime_freq + 1);
	features["lifetime_freq_log_std"] = common::RunningMeanNormalize(
		log(data.lifetime_freq + 1), params->rm_lifetime_freq_log
	);

	return features;
}

void common::obj_metadata::Reset() {
	rtime_since = 0;
	obj_size_relative = 0;
	clock_freq = 0;
	rtime_between = 0;
	rtime = 0;
	last_access_vtime = 0;
	last_access_rtime = 0;
	obj_size = 0;
	vtime = 0;

	create_rtime = 0;

	first_seen = 0;
	compulsory_miss = 0;
}

void common::obj_metadata::Track(const request_t* req) {
	rtime_between = req->clock_time - rtime;
	rtime = req->clock_time;
	last_access_vtime = req->vtime_since_last_access;
	last_access_rtime = req->rtime_since_last_access;
	obj_size = req->obj_size;
	create_rtime = req->create_rtime;
	first_seen = req->first_seen_in_window;
	compulsory_miss = req->compulsory_miss;
	clock_freq++;
	lifetime_freq++;
}

void common::TrackRunningMean(const float X, RunningMeanData& d) {
	d.n++;
	float d1 = X - d.mean;
	d.mean += d1 / d.n;
	float d2 = X - d.mean;
	d.m2 += d1 * d2;
}

float common::RunningMeanNormalize(const float X, RunningMeanData& d) {
	float variance = d.m2 / (d.n - 1);
	float std = sqrt(variance);
	if (std == 0 || std::isnan(std)) {
		return 0;
	}
	float norm = (X - d.mean) / std;
	return norm;
}

void common::Custom_clock_params::GlobalTrack(const common::obj_metadata& data) {
	if (data.lifetime_freq > max_lifetime_freq) {
		max_lifetime_freq = data.lifetime_freq;
	}

	if (data.clock_freq > max_clock_freq) {
		max_clock_freq = data.clock_freq;
	}

	if (data.rtime_between > max_rtime_between) {
		max_rtime_between = data.rtime_between;
	}

	if (data.rtime_since > max_rtime) {
		max_rtime = data.rtime_since;
	}

	TrackRunningMean(data.clock_freq, rm_clock_freq);
	TrackRunningMean(data.lifetime_freq, rm_lifetime_freq);
	TrackRunningMean(data.rtime_between, rm_rtime_between);

	TrackRunningMean(log(data.clock_freq + 1), rm_clock_freq_log);
	TrackRunningMean(log(data.lifetime_freq + 1), rm_lifetime_freq_log);
	TrackRunningMean(log(data.rtime_between + 1), rm_rtime_between_log);
}
