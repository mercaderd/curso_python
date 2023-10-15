# -*- coding: utf-8 -*-

"""
Some utils functions
"""

import string
import secrets
import sys


def password_gen(length,
                 alphabet = string.punctuation
                 + string.ascii_lowercase
                 + string.ascii_uppercase
                 + string.digits):
    '''Genera una contraseña segura de longitud length
        Parámetros por clave opcionales: 
        alphabet: Cadena con caracteres a utilizar en la contraseña. 
        Por defecto, signos de puntuación, minúsculas, mayúsculas y números
    '''

    password = ''
    for i in range(length):
        password += secrets.choice(alphabet)
    return password


if __name__ == '__main__':
    print(password_gen(length = int(sys.argv[1])))
