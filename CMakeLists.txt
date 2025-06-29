cmake_minimum_required(VERSION 3.14)
project(cacheSimulator)

message(
  "****************** this example only works after libCacheSim has been installed ******************"
)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

find_library(libCacheSim libCacheSim)
find_path(libCacheSimInclude libCacheSim)
message(STATUS "libCacheSim found? ${libCacheSim} ${libCacheSimInclude}")
include_directories(${libCacheSimInclude})

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_SOURCE_DIR}/cmake/Modules/")
find_package(GLib "2.40" REQUIRED)
include_directories(${GLib_INCLUDE_DIRS})
message(
  STATUS
    "glib found? ${GLib_FOUND}, lib = ${GLib_LIBRARY}, header = ${GLib_INCLUDE_DIRS}"
)

find_package(ZSTD)
# https://stackoverflow.com/questions/61377055/cannot-find-gflags-gflags-h-while-building-library-osx/61379123#61379123
include_directories(${ZSTD_INCLUDE_DIR})
if("${ZSTD_LIBRARIES}" STREQUAL "")
  message(FATAL_ERROR "zstd not found")
endif()

find_library(ONNXRUNTIME_LIB onnxruntime)
find_path(onnxruntimeInclude onnxruntime)
message(STATUS "ONNX runtime found? ${onnxruntime} ${libCacheSimInclude}")
include_directories(onnxruntimeInclude)

add_executable(cacheSimulator
  src/main.cpp
  src/experiment.cpp
  src/cache/common.cpp
  src/cache/offline_clock.cpp
  src/cache/base.cpp
  src/cache/ml_clock.cpp
  src/cache/decayed_clock.cpp
  src/cache/my_clock.cpp
  src/cache/dist_clock.cpp
  src/cache/dram.cpp
)
target_include_directories(cacheSimulator PRIVATE src .)

target_link_libraries(
  cacheSimulator PUBLIC libCacheSim onnxruntime m ${GLib_LIBRARY} ${ZSTD_LIBRARIES}
)
