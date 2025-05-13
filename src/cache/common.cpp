#include "common.hpp"
#include <cmath>
#include <cstdint>
#include <exception>
#include <sys/types.h>

void common::obj_metadata::Reset() {
	lifetime_freq = 0;
	last_promotion = 0;

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

void common::TrackRunningMean(const float X, float& mean, float& m2, uint64_t& n) {
	n++;
	float d1 = X - mean;
	mean += d1 / n;
	float d2 = X - mean;
	m2 += d1 * d2;
}

float common::RunningMeanNormalize(const float X, const float mean, const float m2,
								   const uint64_t n) {
	float variance = m2 / (n - 1);
	float std = sqrt(variance);
	float norm = (X - mean) / std;
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

	TrackRunningMean(data.clock_freq, mean_clock_freq, m2_clock_freq, n_clock_freq);
	TrackRunningMean(data.lifetime_freq, mean_lifetime_freq, m2_lifetime_freq, n_lifetime_freq);
}
