import requests
from bs4 import BeautifulSoup

headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Cookie': 'cookie-agreed=0',
        'Upgrade-Insecure-Requests': '1'
    }

url = 'https://www.aepd.es/informes-y-resoluciones/resoluciones'
req = requests.get(url, headers=headers)
print(req.url)
if req.status_code == 200:
    html = BeautifulSoup(req.text, 'html.parser') # Beautiful Soup para parsear el html y poder buscar elementos
    resoluciones = html.find_all('div', {'class': 'layout__region--content'})
    for resolucion in resoluciones:
        titulo = ''
        link = ''
        fecha = ''
        tag_titulo = resolucion.find('div', {'class': 'field--name-title'})
        if tag_titulo:
            titulo = tag_titulo.getText()
        tag_link = resolucion.find('a',{'class': ''})
        print(tag_link)
        if tag_link:
            link = 'https://www.aepd.es' + tag_link['href']
        tag_fecha = resolucion.find('time')
        if tag_fecha:
            fecha = tag_fecha['datetime']
        print((titulo,link,fecha))


# Descargar archivo con requests
# with requests.get(url, stream = True) as r:
                            # with open(dataPath + titulo, 'wb') as f:
                            #     for chunk in r.iter_content(chunk_size=1024):
                            #         f.write(chunk)            