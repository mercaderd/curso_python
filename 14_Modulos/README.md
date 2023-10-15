# 📗 Lección 14: Modulos y Paquetes

**[Índice](../README.md)**

**[Anterior](../13_Funciones/README.md)**

## Módulos

### Definición

Un módulo es un archivo *.py* que contiene un conjunto de funciones y/o clases, que puede importarse desde otro módulo o que puede ejecutarse.

### Creación de un módulo

Para crear un módulo se meten nuevas funciones/clases en un archivo *.py*, por ejemplo en un archivo *utils.py*:

```python
# file utils.py

import strings
import secrets


def password_gen(length, alphabet = string.punctuation + string.ascii_lowercase + string.ascii_uppercase + string.digits):
    '''Genera una contraseña segura de longitud length
        Parámetros por clave opcionales:
        alphabet: Cadena con caracteres a utilizar en la contraseña. Por defecto, signos de puntuación, minúsculas, mayúsculas y números'''
    password = ''
    for i in range(length):
        password += secrets.choice(alphabet)
    return password
```

### Importando un módulo

Desde otro fichero *.py* en el mismo directorio se puede importar el módulo utilizando *import* y llamar a las funciones clases incluídas.

```python
# file main.py
import utils

print(utils.password_gen(length = 10))
```

Cuando se importa un módulo se le puede poner un álias que facilite su utilización en el resto del código.

```python
# file main.py
import utils as ut

print(ut.password_gen(length = 10))
```

Tambien pueden importarse únicamente algunas funciones/clases de un módulo.

```python
# file main.py
from utils import password_gen

print(password_gen(length = 20))
```

### Identificando si un módulo se ejecuta independientemente o es importado

El atributo *__name__* da acceso al nombre del módulo, pero si el módulo es ejecutado independientemente el atributo tendrá el valor *'__main__'* en vez de el nombre del módulo. Esto permite definir cómo debe ejecutarse el módulo cuando se ejecuta de forma independientes.

```python
#file utils.py
# -*- coding: utf-8 -*-

"""
Some utils functions
"""

import string
import secrets


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

# Lo que hay a partir del siguiente if únicamente se ejutará si el módulo es lanzado directamente, pero no si el módulo es importado
if __name__ == '__main__':
    print(password_gen(length = 10)) 
```

### Importando algunos módulos Built-in

#### Módulo OS

Con el módulo *OS* se pueden realizar muchas taréas típicas de sistema operativo.

```python
# import the module
import os
# Creating a directory
os.mkdir('directory_name')
# Changing the current directory
os.chdir('path')
# Getting current working directory
os.getcwd()
# Removing directory
os.rmdir()
```

#### Módulo SYS

El módulo *sys* proporciona funciones y variables del entorno de ejecución de python. La función *sys.argv* devuelve una lista de argumentos de línea de comandos pasados a un script de Python. El elemento en el índice 0 de esta lista es siempre el nombre del script, en el índice 1 está el argumento pasado desde la línea de comandos.

```python
# file utils.py
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
```



**[Siguiente](../15_EntornosVirtuales/README.md)**
