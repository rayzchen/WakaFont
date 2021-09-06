#!/bin/bash

TOKEN=""

curl "https://api.wanikani.com/v2/subjects/?types=radical" \
  -H "Authorization: Bearer $TOKEN"
