import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urlparse


headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Cookie': 'cookie-agreed=0',
        'Upgrade-Insecure-Requests': '1'
    }


def download(url, filepath):
    with requests.get(url, stream = True, timeout=200) as r:
        with open(filepath, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                f.write(chunk)



url = '' # TODO: Rellenar url objetivo
parsed_url = urlparse(url)
req = requests.get(url, headers=headers, timeout=200)
if req.status_code == 200:
    html = BeautifulSoup(req.text, 'html.parser') # Beautiful Soup para parsear el html y poder buscar elementos
    with open('./datos.csv', mode='wt', encoding='utf-8') as f:
        csv_file = csv.writer(f, delimiter = ',')
        csv_file.writerow(['titulo', 'enlace', 'fecha'])
        resoluciones = html.find_all('div', {'class': 'layout__region--content'})
        for resolucion in resoluciones:
            titulo = ''
            link = ''
            fecha = ''
            tag_titulo = resolucion.find('div', {'class': 'field--name-title'})
            if tag_titulo:
                titulo = tag_titulo.getText()
            tag_link = resolucion.find('a',{'class': ''})
            if tag_link:
                link = f'{parsed_url.scheme}://{parsed_url.hostname}/' + tag_link['href']
            tag_fecha = resolucion.find('time')
            if tag_fecha:
                fecha = tag_fecha['datetime']
            if all([titulo,link,fecha]):
                csv_file.writerow([titulo, link, fecha])
                download(link, f"{titulo}.pdf")