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

url = 'https://api.mailgun.net/v3/' + DOMAIN + '/bounces/%s'

for line in sys.stdin:
    email = line.strip()
    if not email:
        continue
    resp = s.delete(
        url % (email),
        auth=('api', API_KEY)
    )
    if resp.status_code != 200:
        print(email + '\t' + resp.status_code + '\t' + resp.text)
