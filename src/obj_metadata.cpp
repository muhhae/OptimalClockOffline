#include "obj_metadata.hpp"

thread_local uint64_t n_hit = 0;
thread_local uint64_t n_req = 0;
thread_local uint64_t n_promoted = 0;
thread_local std::unordered_map<obj_id_t, obj_metadata> objs_metadata;
