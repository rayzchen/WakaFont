#!/usr/bin/python3

import json
import urllib.request

# https://api.wanikani.com/v2/subjects/?types=radical
with open('radicals.json') as f:
    rads = json.load(f)['data']

for r in rads:
    rdata = r['data']
    if rdata['characters'] is not None:
        continue

    img_url = next(i for i in rdata['character_images']
                   if i['content_type'] == 'image/png' and
                      i['metadata']['color'] == '#000000' and
                      i['metadata']['dimensions'] == '1024x1024')['url']

    meaning = rdata['meanings'][0]['meaning'].lower().replace(' ', '-')
    urllib.request.urlretrieve(img_url, 'png/' + meaning)
