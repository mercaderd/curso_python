# -*- coding: utf-8 -*-

import requests
import json
from docxtpl import DocxTemplate
import sys


API_URL = 'https://urlscan.io/api/v1/'

SUBMIT = 'scan/'
RESULT = 'result/'
SEARCH = 'search/?q=domain:'

def submit(apikey, url):
    """ Documentar"""
    # TODO: Completar DOCSTRING
    # TODO: Validar url antes de seguir
    headers = {'API-Key':apikey,'Content-Type':'application/json'}
    data = {"url": url, "visibility": "public"}
    r = requests.post(API_URL+SUBMIT, headers=headers, data=json.dumps(data), timeout=200)
    return r.status_code, r.json()
    

def result(apikey, uuid):
    """ Documentar"""
    # TODO: Completar DOCSTRING
    # TODO: Validar uuid antes de seguir
    headers = {'API-Key':apikey,'Content-Type':'application/json'}
    r = requests.get(API_URL+RESULT+uuid, headers=headers, timeout=200)
    return r.status_code, r.json()
    

def search(apikey, domain):
    """ Documentar"""
    # TODO: Completar DOCSTRING
    # TODO: Validar domain antes de seguir
    headers = {'API-Key':apikey,'Content-Type':'application/json'}
    r = requests.get(API_URL+SEARCH+domain, headers=headers, timeout=200)
    return r.status_code, r.json()

def report(apikey, uuid):
    """ Documentar"""
    # TODO: Completar DOCSTRING
    # TODO: Validar uuid antes de seguir
    headers = {'API-Key':apikey,'Content-Type':'application/json'}
    r = requests.get(API_URL+RESULT+uuid, headers=headers, timeout=200)
    if r.status_code == requests.codes.ok:
        doc = DocxTemplate("./template.docx")
        doc.render(r.json())
        doc.save("./output.docx")
    return r.status_code, r.json()


if __name__ == "__main__":
    if len(sys.argv) < 4:
        sys.exit("Debe llamar con urlscan.py $apikey [submit,result,search,report] [$url,$uuid,$domain,$uuid]")
    if sys.argv[2] == 'submit':
        print(submit(apikey=sys.argv[1], url=sys.argv[3]))
    elif sys.argv[2] == 'result':
        print(result(apikey=sys.argv[1], uuid=sys.argv[3]))
    elif sys.argv[2] == 'search':
        print(search(apikey=sys.argv[1], domain=sys.argv[3]))
    elif sys.argv[2] == 'report':
        print(report(apikey=sys.argv[1], uuid=sys.argv[3]))
    else:
        sys.exit("Debe llamar con urlscan.py $apikey [submit,result,search,report] [$url,$uuid,$domain,$uuid]")

