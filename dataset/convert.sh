#!/bin/sh

# fail fast in case of error
set -e
set -o pipefail

echo "============================================="
echo "======== creating lexical dataset ==========="
echo "============================================="
python3 convert.py > weather.json
echo "Done! lexical dataset written to weather.json"
echo
echo "============================================="
echo "======== creating word2vec dataset =========="
echo "============================================="
python3 convert-to-w2v.py > weather-w2v.json
echo "Done! word2vec dataset written to weather-w2v.json"
echo
echo "============================================="
echo "======== creating doc2vec dataset ==========="
echo "============================================="
python3 convert-to-d2v.py > weather-d2v.json
echo "Done! doc2vec dataset written to weather-d2v.json"
