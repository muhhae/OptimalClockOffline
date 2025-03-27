#!/bin/bash

sudo apt install gh libglib2.0-dev cmake python3.10-venv &&
    cd ~ && git clone https://github.com/1a1a11a/libCacheSim &&
    cd libCacheSim && mkdir _build && cd _build && cmake .. &&
    make -j && sudo make install

cd ~ &&
    cd ~/OptimalClockOffline/python &&
    python -m venv .venv && .venv/bin/pip install -r requirement.txt &&
    cd ~/OptimalClockOffline && gh auth login && gh auth setup-git
