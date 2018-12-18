#!/bin/sh

python3 preprocess/tangshisanbaishou.py
python3 preprocess/quantangshi.py
python3 preprocess/yuefushiji.py
python3 preprocess/filter_poet.py 5
python3 preprocess/filter_poet.py 7
