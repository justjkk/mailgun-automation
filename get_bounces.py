from __future__ import print_function
import json
import requests
import os
import sys

API_KEY = os.getenv('MAILGUN_API_KEY')
if not API_KEY:
    print('Expecting MAILGUN_API_KEY environment variable')
    sys.exit(1)

DOMAIN = os.getenv('MAILGUN_DOMAIN')
if not DOMAIN:
    print('Expecting MAILGUN_DOMAIN environment variable')
    sys.exit(1)

s = requests.Session()

url = 'https://api.mailgun.net/v3/' + DOMAIN + '/bounces'
last_url = url + '?limit=100'
while True:
    resp = s.get(
        url,
        auth=('api', API_KEY)
    )

    jdata = resp.json()
    for item in jdata['items']:
        print(item['address'])
    url = jdata['paging']['next']
    if url == last_url:
        break
