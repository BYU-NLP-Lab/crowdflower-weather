#!/bin/sh

# fail fast
set -e

TMP=extra-weather-tweets

echo "concatenating all extra weather tweets"
~/git/utils/json_objects/append.py $TMP/* > /tmp/ewt1.json
echo "translating tweets into dataset format"
~/git/utils/annotation_streams/twitter/json2stream.sh /tmp/ewt1.json > /tmp/ewt2.json
echo "translating links to {link}"
~/git/utils/json_objects/translate.py /tmp/ewt2.json --attr data --before "https?:[^\s]*"  --after "{link}" > /tmp/ewt3.json
echo "translating mentions to @mention"
~/git/utils/json_objects/translate.py /tmp/ewt3.json --attr data --before "@[^\s]*"  --after "@mention" > /tmp/ewt4.json
echo "appending tweets to dataset"
~/git/utils/json_objects/append.py ../weather.json /tmp/ewt4.json > weather-augmented.json

echo "dataset augmented with tweets is available in weather-augmented.json"
