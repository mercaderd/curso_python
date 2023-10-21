# 📗 Lección 18: Web Scrapping

**[Índice](../README.md)**

**[Anterior](../17_HTTP/README.md)**

# Hacer una petición GET con parámetros
# https://www.axesor.es/buscar/empresas?tabActivo=empresas&q=Q2813014D
params = {'tabActivo': 'empresas', 'q': 'Q2813014D'}

r = requests.get('https://www.axesor.es/buscar/empresas', params=params)
print(r.url)
print(r.status_code)

**[Siguiente](../19_/Objetos.md)**
