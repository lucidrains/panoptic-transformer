#!/usr/bin/env bash

[ ! -d 'pathfinder' ] && git clone https://github.com/drewlinsley/pathfinder.git
apt-get install ffmpeg libsm6 libxext6 gfortran libopenblas-dev liblapack-dev -y
pip install -r requirements.txt
cp scripts/gen-pathx.py ./pathfinder
python pathfinder/gen-pathx.py 1 1 25000
