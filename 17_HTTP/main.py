# HTTP Requests

import requests
import json

# Hacer una petición GET

r = requests.get('https://www.aepd.es')
print(r.status_code)
print(r.request.headers)
print(r.headers)
if r.status_code == requests.codes.ok:
    print(r.text)


# Primera petición a una API

r = requests.get('https://fakestoreapi.com/este-endpoint-no-existe')
print(r.status_code) # 404 Error porque el endpoint no existe

r = requests.get('https://fakestoreapi.com/products')
if r.status_code == requests.codes.ok:
    print(type(r.json()))
    print(json.dumps(r.json()[0:2],indent=4))



