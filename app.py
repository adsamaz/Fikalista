import requests
import json

import time

url = 'http://chatt.sfa.se/hooks/4o1sdns6qj8z7b37xtfmrgwxuy'
payload = {'Content-Type': 'application/json', 'text': 'Testing testing :tada:'}

# GET
#r = requests.get(url)

# GET with params in URL
#r = requests.get(url, params=payload)

# POST with form-encoded data
#r = requests.post(url, data=paylo  ad)

# POST with JSON

while True:
    #r = requests.post(url, data=json.dumps(payload))
    print("Sent message")
    #print(r.text)
    #print(r.status_code)
    time.sleep(20) # Delay for 20 seconds
    

