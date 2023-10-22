 # -*- coding: utf-8 -*-

import urlscan


apikey = '' # API Key no es necesaria para pedir resultados

if __name__ == '__main__':
    print(urlscan.result(apikey=apikey, uuid='8a8b07b8-d467-4bce-a28d-7764c7950792'))