# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re

URL = 'https://www.axesor.es/buscar/empresas'
#NIF_RE = '\d{8}[A-Za-z]'
CIF_RE = '[ABCDEFGHJKLMNPQRSUVW]\d{7}[0-9A-J]'

headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Cookie': 'cookie-agreed=0',
        'Upgrade-Insecure-Requests': '1'
    }

def get(nif):
    """Documentar"""
    # TODO: Documentar
    # TODO: Validar nif
    result = None
    validator = re.compile(CIF_RE)
    if not validator.match(nif):
        return result
    params = {
        'tabActivo': 'empresas',
        'q': nif
    }
    r = requests.get(URL, headers=headers, params=params, timeout=1000)
    if r.status_code == requests.codes.ok:
        html = BeautifulSoup(r.text,'html.parser')
        #print(html.prettify())
        tabla = html.find('table', {'id': 'tablaInformacionGeneral'})
        if tabla:
            datos = {}
            lineas = tabla.find_all('tr')
            for linea in lineas:
                if linea.td.string and linea.td.next_sibling:
                    datos[linea.td.string.strip()] = linea.td.next_sibling.string.strip() if linea.td.next_sibling.string else None
            result = datos
    return datos


def gets(nifs):
    """Documentar"""
    # TODO: Documentar
    result = []
    for nif in nifs:
        result.append(get(nif))
    return result


if __name__ == "__main__":
    print(gets(['Q2813014D', 'A82018474']))