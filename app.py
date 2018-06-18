import requests
import json

import time

url = 'http://chatt.sfa.se/hooks/4o1sdns6qj8z7b37xtfmrgwxuy'
payload = {'Content-Type': 'application/json', 'text': 'Testing testing :tada:'}

a = True
# GET
#r = requests.get(url)

# GET with params in URL
#r = requests.get(url, params=payload)

# POST with form-encoded data
#r = requests.post(url, data=paylo  ad)

# POST with JSON

if a:
    #r = requests.post(url, data=json.dumps(payload))
    a = False
    # Response, status etc
    #print(r.text)
    #print(r.status_code)
    print("Hello World")

while True:
    print("Hello World")
    time.sleep(5) # Delay for 1 minute (60 seconds).

