#!/bin/sh

mkdir base/cache
mkdir base/log

python2 ./bin/start.py

rm -r base/cache