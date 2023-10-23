import requests
from bs4 import BeautifulSoup

headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
        #'DNT': '1',
        #'Connection': 'keep-alive',
        #'Cookie': 'cookie-agreed=0',
        #'Upgrade-Insecure-Requests': '1'
    }

url = ''
req = requests.get(url, headers=headers)
if req.status_code == 200:
    print(req.status_code)
    html = BeautifulSoup(req.text, 'html.parser') # Beautiful Soup para parsear el html y poder buscar elementos
    print(req.text)
    #fines = html.find_all("div", {'class': ''})
    #print(fines)
    #for fine in fines:
    #    pass