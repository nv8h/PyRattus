#!/bin/sh

mkdir base/cache
mkdir base/log

python2 ./bin/start.py service $*

rm -r base/cache