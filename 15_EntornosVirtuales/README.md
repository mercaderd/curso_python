# 📗 Lección 15: Gestor de paquetes y entornos virtuales

**[Índice](../README.md)**

**[Anterior](../14_Modulos/README.md)**

## Gestor de paquetes PIP

*Python pip* es el gestor de paquetes de python y se utiliza para instalar/desinstalar fácilmente paquetes en una instalación de python o en un entorno virtual. No es el único gestor de paquetes de Python, pero sí el mas extendido.

### Instalar paquetes

Generalmente *pip* vendrá instalado en cualquier distribución de python. Para comprobar si *pip* esta instalado se puede ejecutar:

```console
$ pip --version
pip 23.2.1 from /usr/local/python/3.10.8/lib/python3.10/site-packages/pip (python 3.10)
```

Instalar un paquete es muy sencillo, por ejemplo vamos a instalar el paquete *requests*, utilizado para trabajar con perticiones HTTP de forma sencilla.

```console
$ pip install requests
Requirement already satisfied: requests in /home/codespace/.local/lib/python3.10/site-packages (2.31.0)
Requirement already satisfied: charset-normalizer<4,>=2 in /home/codespace/.local/lib/python3.10/site-packages (from requests) (3.2.0)
Requirement already satisfied: idna<4,>=2.5 in /home/codespace/.local/lib/python3.10/site-packages (from requests) (3.4)
Requirement already satisfied: urllib3<3,>=1.21.1 in /home/codespace/.local/lib/python3.10/site-packages (from requests) (2.0.5)
Requirement already satisfied: certifi>=2017.4.17 in /home/codespace/.local/lib/python3.10/site-packages (from requests) (2023.7.22)

[notice] A new release of pip is available: 23.2.1 -> 23.3
[notice] To update, run: python -m pip install --upgrade pip
```

En el ejemplo anterior, requests ya estaba instalado en el sistema. Pero de no haberlo estado se hubiera instalado.

### Listar paquetes instalados

Para listar los paquetes instalados se utiliza *pip list*.

```console
$ pip list
Package                   Version
------------------------- ------------
anyio                     4.0.0
argon2-cffi               23.1.0
argon2-cffi-bindings      21.2.0
arrow                     1.2.3
asttokens                 2.4.0
async-lru                 2.0.4
attrs                     23.1.0
Babel                     2.12.1
...
...
```

### Obtener información sobre un paquete

Se obtiene información sobre un paquete con *pip show*.

```console
$ pip show requests
Name: requests
Version: 2.31.0
Summary: Python HTTP for Humans.
Home-page: https://requests.readthedocs.io
Author: Kenneth Reitz
Author-email: me@kennethreitz.org
License: Apache 2.0
Location: /home/codespace/.local/lib/python3.10/site-packages
Requires: certifi, charset-normalizer, idna, urllib3
Required-by: jupyterlab_server, nbdime
```

## Entornos virtuales

Los entornos virtuales permiten crear una instalación de python aislada de la instalación principal en nuestro sistema e instalar paquetes de forma independientes. Esto facilita la gestión de dependencias cuando se esta desarrollando un proyecto, especialmente si se tiene pensado distribuir la aplicación a otros usuarios.

Ventajas:
- Tener varios entornos, con varios conjuntos de paquetes, sin conflictos entre ellos. De esta manera, los requisitos de diferentes proyectos se pueden satisfacer al mismo tiempo.
- Lanzar fácilmente proyectos con sus propios módulos dependientes.
- Permite gestionar los paquetes necesarios para el proyecto independientemente de otros proyectos y de la instalación principal de python del sistema.
- Distribuir las aplicaciones con el mínimo de paquetes necesarios para su funcionamiento y en las versiones correctas.

### Crear un entorno virtual y activarlo

Una buena práctica al iniciar un proyecto, es crear un entorno virtual en la carpeta del proyecto.

```console
$ cd proyecto1
$ python -m venv my_venv
```
Se creará una carpeta *my_venv* que contiene el entorno virtual (una instalación de python independiente de otros entornos y de la instalación principal de python)

Despues de crear el entorno virtual es necesario activarlo para trabajar en el entorno virtual.

En linux:
```console
$ source my_venv\bin\activate
(my_venv) $
```

En Windows PowerShell:
```console
C:\Users\User\Documents\user1\proyecto1> my_venv\Scripts\activate
(my_venv) C:\Users\User\Documents\user1\proyecto1>
```

En Windows Cmd:
```console
C:\Users\User\Documents\user1\proyecto1> my_venv\Scripts\Activate.bat
(my_venv) C:\Users\User\Documents\user1\proyecto1>
```

Una vez creado y activado, se pueden instalar los paquetes necesarios para el proyecto que se está desarrollando con *pip install nombrepaquete*.

### Fichero requirements.txt

En general los entornos virtuales ocupan bastante espacio y tienen muchos ficheros, por lo que no suelen distribuirse con el código de las aplicaciones o cuando se publican en GitHub. En su lugar, lo que se incluye es un fichero *requirements.txt* con la lista de paquetes necesarios y su versión.

Una vez activado el entorno virtual e instalados los paquete necesarios para el proyecto, se puede crear el fichero *requirements.txt* con *pip freeze*.

```console
(my_venv) $ pip freeze > requirements.txt
```
Si el fichero *requirements.txt* está disponible, se pueden instalar todos los paquetes necesarios de una sola vez con el siguiente comando:

```console
(my_venv) C:\Users\User\Documents\user1\proyecto1> pip install -r requirements.txt
```




**[Siguiente](../16_Ficheros/README.md)**
