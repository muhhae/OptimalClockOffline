#pragma once

#include <cstdint>
#include <fstream>
#include <libCacheSim/cache.h>
#include <libCacheSim/cacheObj.h>
#include <libCacheSim/evictionAlgo.h>
#include <libCacheSim/request.h>
#include <unordered_map>
#include <unordered_set>

namespace cclock {
void clear_cache(cache_t *c);

struct req_metadata {
  req_metadata() = default;
  void Track(const request_t *req) {
    clock_time_between = req->clock_time - clock_time;
    clock_time = req->clock_time;
    last_access_vtime = req->vtime_since_last_access;
    last_access_rtime = req->rtime_since_last_access;
    obj_size = req->obj_size;
    create_rtime = req->create_rtime;
    first_seen = req->first_seen_in_window;
    compulsory_miss = req->compulsory_miss;
  }

  int64_t clock_time_between = 0;
  int64_t clock_time = 0;
  int64_t last_access_vtime = 0;
  int64_t last_access_rtime = 0;
  int64_t obj_size = 0;

  int32_t create_rtime = 0;

  bool first_seen = 0;
  bool compulsory_miss = 0;
};

struct obj_metadata {
  uint64_t access_counter = 0;
  uint64_t last_promotion = 0;
  req_metadata current_req_metadata;
  std::unordered_set<uint64_t> wasted_promotions;
};

class Custom_clock_params : public Clock_params_t {
public:
  Custom_clock_params() = default;
  Custom_clock_params(const Clock_params_t &base) {
    *(Clock_params_t *)this = base;
  }

public:
  std::ofstream datasets;
  std::unordered_map<obj_id_t, obj_metadata> objs_metadata;

  uint64_t n_hit;
  uint64_t n_req;
  uint64_t n_promoted;

  bool generate_datasets;
};

cache_t *CustomClockInit(const common_cache_params_t ccache_params,
                         const char *cache_specific_params);
cache_t *TestClockInit(const common_cache_params_t ccache_params,
                       const char *cache_specific_params);
} // namespace cclock
