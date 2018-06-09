#!/bin/sh
TMP=extra-weather-tweets

mkdir -p $TMP
~/git/utils/twitter/harvest.py --search weather > $TMP/`date +%s`.json
