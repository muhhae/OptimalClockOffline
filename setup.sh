#!/bin/bash

sudo apt install -y libglib2.0-dev libzstd-dev cmake python3.10-venv
cd .. && [ ! -d libCacheSim ] && git clone https://github.com/1a1a11a/libCacheSim &&
cd libCacheSim && mkdir -p _build && cd _build && cmake .. &&
make -j && sudo make install &&
cd ../.. &&
cd OptimalClockOffline/python &&
python -m venv .venv && .venv/bin/pip install -r requirement.txt &&
cd .. && mkdir build && cd build && cmake .. && make .
