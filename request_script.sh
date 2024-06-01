#!/bin/bash

while true; do
  curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"url": "https://www.phaidra.ai/"}' \
  http://localhost:55001/
  sleep 5
done
