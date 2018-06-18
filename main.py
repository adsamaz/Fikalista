import requests
import json

url = 'http://chatt.sfa.se/hooks/4o1sdns6qj8z7b37xtfmrgwxuy'
payload = {'Content-Type': 'application/json', 'text': 'Testing testing :tada:'}

a = True
# GET
#r = requests.get(url)

# GET with params in URL
#r = requests.get(url, params=payload)

# POST with form-encoded data
#r = requests.post(url, data=payload)

# POST with JSON

if a:
    r = requests.post(url, data=json.dumps(payload))
    a = False
    # Response, status etc
    print(r.text)
    print(r.status_code)


