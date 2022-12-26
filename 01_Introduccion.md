# Lección 01: Introducción

## ¿Qué es Python?

### Python es un lenguaje de programación potente y fácil de aprender

Python es un lenguaje de programación interpretado (el código no se compila) con una sintaxis muy sencilla (en comparación con otros lenguajes clásicos) y que pretende que el código sea muy limpio.

Es un lenguaje sencillo, fácil, muy legible y con una curva de aprendizaje muy buena, por lo que es una buena opción para aprender a programar desde cero.

El origen de Python se remonta a los 90, creado por el holandés Gudo van Rossum y que le puso el nombre en honor a una serie de televisión creada por el grupo cómico Monty Python (La vida de Brian).

Es el lenguaje de programación más popular en los últimos años (en dura pugna con Javascript según el ranking que se consulte).

![Ranking lenguajes programación 2022](https://www.stackscale.com/wp-content/uploads/2022/09/popular-programming-languages-ranking-2022.jpg)

Algunos proyectos/empresas populares que utilizan Python en sus productos son:
- Instagram
- Google App Engine
- Pinterest
- Facebook
- Dropbox
- Battelfield
- Spotify
- Netflix
- NASA

### Características principales:
- Interpretado
- Tipado dinámico
- Alto nivel
- Orientado a objetos
- Multiplataforma
- Organizado y extensible (Clases, Módulos, Paquetes, Bibliotecas, Frameworks)

### Ventajas:
- Sintaxis simple y sencilla, cercana al lenguaje natural y fácil de interpretar por cualquiera con mínimos conocimientos de programación.
- Lenguaje muy potente, se puede hacer mucho con menos líneas de código que en cualquier otro lenguaje. Desarrolladores muy productivos.
- Gran biblioteca estándar con código reutilizable y muy amplia variedad de bibliotecas disponibles (para casi cualquier cosa que se quiera hacer).
- Fácilmente integrable con otros lenguajes de programación.
- Comunidad muy activa. Muy fácil encontrar recursos en internet.
- Muy utilizado investigación científica, ciencia de datos, aprendizaje automático, inteligencia artificial, ciberseguridad, ...

### Desventajas:
- No adecuado para muchas aplicaciones en Tiempo Real (Real Time Programming).
- Poco usable en desarrollo web lado del cliente o frontend (En esto Javascript gana por goleada!!).
- Hay que tener cuidado con las bibliotecas que se utilizan.

### ¿En qué se utiliza Python?:
- Desarrollo web lado del servidor - Backend (Flask, Django, FastAPI).
- Automatización de tareas con scripts.
- Ciencia de datos y aprendizaje automático (TensorFlow, Keras, scikit-learn).
- Desarrollo de software.
- Automatización de pruebas de software.

### Versiones de python
- Python 1 - Publicado en 1994 - Obsoleto.
- Python 2 - Publicado en 2000 - Comenzó a hacerse popular en esta versión. Se sigue utilizando en muchas aplicaciones ya desarrolladas, pero es una versión obsoleta.
- Python 3 - Publicado en 2008 - Versión actual de Python. Versión que debe utilizarse para cualquier nueva aplicación y que utilizaremos en este curso. 

## Instalar Python y un entorno de desarrollo
Para empezar a utilizar Python es necesario instalar:
- Python 3 (Intérprete + biblioteca estandar).
- Un IDE o Entorno de desarrollo. Puede ser algo tan básico como un simple editor de texto o un entorno de desarrollo más complejo que incluya comprobación de sintaxis, herramientas de depuración y otras ayudas que facilitan el desarrollo.

### Instalar Python 3
Se puede intalar Python (intérprete + biblioteca estándar) desde la web oficial [python.org](https://www.python.org/downloads/). Es la instalación más básica que se puede hacer.

> **Nota**:
> Si el objetivo es trabajar en ciencia de datos, aprendizaje automático o similar, se puede instalar alguna plataforma integrada como [Anaconda](https://www.anaconda.com/), que incluirá el intérprete de Python, la biblioteca estándar y una amplia colección de bibliotecas para ciencia de datos, aprendizaje automático, inteligencia artificial, etc. 

### Entorno de desarrollo
Los entornos de desarrollo mas populares para Python son:
- [Pycharm](https://www.jetbrains.com/es-es/pycharm/)
- [Visual Studio Code](https://code.visualstudio.com/) o su versión de código abierto [VSCodium](https://vscodium.com/)

Sigue este tutorial de Microsoft para [Instalar Python y VSCode en tu ordenador Windows](https://learn.microsoft.com/es-es/windows/python/beginners)

## Opción para no instalar nada en tu ordenador: Github y Codespaces
Github es un portal para alojar código de cualquier desarrollador utilizando el control de versiones Git. Github ofrece además la posibilidad de utilizar un entorno de desarrollo con Visual Studio Code en la nube, llamado Codespaces. La versión gratuita de Github permite alojar proyectos en repositorios públicos o privados, y la versión gratuita de Codespaces permite disfrutar de 60 horas al mes de entorno de desarrollo en la nube desde cualquier navegador web. Esto es ideal para cualquiera que se quiera introducir al mundo del desarrollo y no quiera/pueda instalar nada en el dispositivo que va a utilizar.

De forma resumida, los pasos a seguir serán:
1. Crear una cuenta en [Github](https://github.com)
2. Crear un [repositorio](https://docs.github.com/es/get-started/quickstart/create-a-repo) en Github.
3. Crear un [Codespace](https://docs.github.com/es/codespaces/developing-in-codespaces/creating-a-codespace-for-a-repository) a partir del repositorio.
4. Comenzar a desarrollar.

Más detalles en la [siguiente](02_Repo_Codespaces.md) lección.

> **Nota 1**:
> Antes de cerrar el navegador no olvides sincronizar los cambios con el repositorio de Github desde Visual Studio Code.

> **Nota 2**:
> Al finalizar cada sesión de trabajo, elimina o para tu Codespace para no alcanzar el límite de 60 horas gratuitas cuando no estás trabajando con el.

## Recursos de aprendizaje

- [Tutorial oficial de Python](https://docs.python.org/es/3/tutorial/).
- Repo [Cursos de Python desde cero](https://github.com/mouredev/Hello-Python) de Mouredev. Repositorios en Github + Vídeos.
- Repo [30 días de Python](https://github.com/Asabeneh/30-Days-Of-Python).
- [Python for Everybody](https://www.py4e.com/)