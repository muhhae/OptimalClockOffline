#pragma once

#include_next <libCacheSim/request.h>
#include <stdint.h>
#include <unordered_map>
#include <unordered_set>

struct obj_metadata {
  uint64_t access_counter = 0;
  uint64_t last_promotion = 0;
  std::unordered_set<uint64_t> wasted_promotions;
};

extern thread_local uint64_t n_hit;
extern thread_local uint64_t n_req;
extern thread_local uint64_t n_promoted;
extern thread_local std::unordered_map<obj_id_t, obj_metadata> objs_metadata;
