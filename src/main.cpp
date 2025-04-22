#include <algorithm>
#include <iostream>
#include <libCacheSim.h>
#include <sys/types.h>
#include <unistd.h>

#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>

#include "experiment.hpp"
#include "lib/CLI11.hpp"

int main(int argc, char **argv) {
  options o;
  CLI::App app{"Offline Clock Simulator, based on libCacheSim"};
  app.add_option("-f,--fixed-cache-sizes", o.fixed_cache_sizes,
                 "Fixed cache sizes in MiB or object count if given "
                 "--ignore-obj-size, can be more than one");
  app.add_option(
      "-r,--relative-cache-sizes", o.relative_cache_sizes,
      "Relative cache sizes in floating number, can be more than one");
  app.add_option("-o,--output-directory", o.output_directory,
                 "Output directory")
      ->default_val("./result");
  app.add_flag("--ignore-obj-size", o.ignore_obj_size,
               "Would ignore object sizes from trace");
  app.add_flag("--generate-datasets", o.generate_datasets,
               "Would generate datasets from simulation");
  app.add_option("-i,--max-iteration", o.max_iteration,
                 "Offline clock max iteration")
      ->default_val(10);
  app.add_option(
      "-d,--description", o.desc,
      "Additional description for experiment, would shows on filename");
  app.add_option("trace_paths", o.trace_paths, "Can be more than one")
      ->required();
  app.add_option("-a,--algo", o.algorithm, "available [default, my, test]")
      ->default_val("default");

  CLI11_PARSE(app, argc, argv);
  std::cout << "Algo " << o.algorithm << "\n";
  RunExperiment(o);
  return 0;
}
