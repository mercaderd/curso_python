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


# Peticiones GET a una API

# Petición a un endpoint inexistente

r = requests.get('https://fakestoreapi.com/este-endpoint-no-existe')
print(r.status_code) # 404 Error porque el endpoint no existe


# Petición correcta

r = requests.get('https://fakestoreapi.com/products')
if r.status_code == requests.codes.ok:
    print(type(r.json()))
    print(json.dumps(r.json()[0:2],indent=4))


# Peticiones GET con parámetros

params = {'limit': 2}
r = requests.get('https://fakestoreapi.com/products', params=params)
print(r.url)  # https://fakestoreapi.com/products?limit=2
if r.status_code == requests.codes.ok:
    print(json.dumps(r.json(),indent=4)) # La API devuelve 2 productos

URL = 'https://fakestoreapi.com/'
ENDPOINT = 'products/'
product_id = 15

url = URL + ENDPOINT + str(product_id)

print(url) # https://fakestoreapi.com/products/15

r=requests.get(url)
if r.status_code == requests.codes.ok:
    print(r.json())
    for key,value in r.json().items():
        print(f'{key}: {value}')


# Petición POST a una API

new_product = {
    "title": 'test product',
    "price": 13.5,
    "description": 'This is just a test product ',
    "image": 'https://i.pravatar.cc',
    "category": 'electronic'
}

URL = 'https://fakestoreapi.com/'
ENDPOINT = 'products/'

url = URL + ENDPOINT

r=requests.post(url, data=new_product)
if r.status_code == requests.codes.ok:
    print(r.json()) # Devuelve el nuevo producto, incluyendo el product_id asignado
    for key,value in r.json().items():
        print(f'{key}: {value}')
    new_product_id = r.json()['id'] # Guardamos la id del producto recien creado

# Petición PUT para modificar un producto

URL = 'https://fakestoreapi.com/'
ENDPOINT = 'products/'

url = URL + ENDPOINT + str(new_product_id)

product_changes = {
    'price': '20.5',
    'category': 'photo'
}

r=requests.put(url, data=product_changes)
if r.status_code == requests.codes.ok:
    print(r.json()) # Devuelve los campos modificados

# Petición DELETE para modificar un producto

r=requests.delete(url)
if r.status_code == requests.codes.ok:
    print(r.json()) # Elimina el producto





