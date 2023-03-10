# 馃摋 Lecci贸n 01: Introducci贸n

**[脥ndice](../README.md)**

## 驴Qu茅 es Python 馃悕?

### Python es un lenguaje de programaci贸n potente y f谩cil de aprender

Python es un lenguaje de programaci贸n interpretado (el c贸digo no se compila) con una sintaxis muy sencilla (en comparaci贸n con otros lenguajes cl谩sicos) y que pretende que el c贸digo sea muy limpio.

Es un lenguaje sencillo, f谩cil, muy legible y con una curva de aprendizaje muy buena, por lo que es una buena opci贸n para aprender a programar desde cero.

El origen de Python se remonta a los 90, creado por el holand茅s Gudo van Rossum y que le puso el nombre en honor a una serie de televisi贸n creada por el grupo c贸mico Monty Python (La vida de Brian).

Es el lenguaje de programaci贸n m谩s popular en los 煤ltimos a帽os (en dura pugna con Javascript seg煤n el ranking que se consulte).

![Ranking lenguajes programaci贸n 2022](https://www.stackscale.com/wp-content/uploads/2022/09/popular-programming-languages-ranking-2022.jpg)

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

### Caracter铆sticas principales:
- Interpretado
- Tipado din谩mico
- Alto nivel
- Orientado a objetos
- Multiplataforma
- Organizado y extensible (Clases, M贸dulos, Paquetes, Bibliotecas, Frameworks)

### Ventajas:
- Sintaxis simple y sencilla, cercana al lenguaje natural y f谩cil de interpretar por cualquiera con m铆nimos conocimientos de programaci贸n.
- Lenguaje muy potente, se puede hacer mucho con menos l铆neas de c贸digo que en cualquier otro lenguaje. Desarrolladores muy productivos.
- Gran biblioteca est谩ndar con c贸digo reutilizable y muy amplia variedad de bibliotecas disponibles (para casi cualquier cosa que se quiera hacer).
- F谩cilmente integrable con otros lenguajes de programaci贸n.
- Comunidad muy activa. Muy f谩cil encontrar recursos en internet.
- Muy utilizado investigaci贸n cient铆fica, ciencia de datos, aprendizaje autom谩tico, inteligencia artificial, ciberseguridad, ...

### Desventajas:
- No adecuado para muchas aplicaciones en Tiempo Real (Real Time Programming).
- Poco usable en desarrollo web lado del cliente o frontend (En esto Javascript gana por goleada!!).
- Hay que tener cuidado con las bibliotecas que se utilizan.

### 驴En qu茅 se utiliza Python?:
- Desarrollo web lado del servidor - Backend (Flask, Django, FastAPI).
- Automatizaci贸n de tareas con scripts.
- Ciencia de datos y aprendizaje autom谩tico (TensorFlow, Keras, scikit-learn).
- Desarrollo de software.
- Automatizaci贸n de pruebas de software.

### Versiones de python
- Python 1 - Publicado en 1994 - Obsoleto.
- Python 2 - Publicado en 2000 - Comenz贸 a hacerse popular en esta versi贸n. Se sigue utilizando en muchas aplicaciones ya desarrolladas, pero es una versi贸n obsoleta.
- Python 3 - Publicado en 2008 - Versi贸n actual de Python. Versi贸n que debe utilizarse para cualquier nueva aplicaci贸n y que utilizaremos en este curso. 

## Instalar Python y un entorno de desarrollo
Para empezar a utilizar Python es necesario instalar:
- Python 3 (Int茅rprete + biblioteca estandar).
- Un IDE o Entorno de desarrollo. Puede ser algo tan b谩sico como un simple editor de texto o un entorno de desarrollo m谩s complejo que incluya comprobaci贸n de sintaxis, herramientas de depuraci贸n y otras ayudas que facilitan el desarrollo.

### Instalar Python 3
Se puede intalar Python (int茅rprete + biblioteca est谩ndar) desde la web oficial [python.org](https://www.python.org/downloads/). Es la instalaci贸n m谩s b谩sica que se puede hacer.

> 馃摑**Nota**:
> Si el objetivo es trabajar en ciencia de datos, aprendizaje autom谩tico o similar, se puede instalar alguna plataforma integrada como [Anaconda](https://www.anaconda.com/), que incluir谩 el int茅rprete de Python, la biblioteca est谩ndar y una amplia colecci贸n de bibliotecas para ciencia de datos, aprendizaje autom谩tico, inteligencia artificial, etc. 

### Entorno de desarrollo
Los entornos de desarrollo mas populares para Python son:
- [Pycharm](https://www.jetbrains.com/es-es/pycharm/)
- [Visual Studio Code](https://code.visualstudio.com/) o su versi贸n de c贸digo abierto [VSCodium](https://vscodium.com/)

Sigue este tutorial de Microsoft para [Instalar Python y VSCode en tu ordenador Windows](https://learn.microsoft.com/es-es/windows/python/beginners)

## Opci贸n para no instalar nada en tu ordenador: Github y Codespaces
Github es un portal para alojar c贸digo de cualquier desarrollador utilizando el control de versiones Git. Github ofrece adem谩s la posibilidad de utilizar un entorno de desarrollo con Visual Studio Code en la nube, llamado Codespaces. La versi贸n gratuita de Github permite alojar proyectos en repositorios p煤blicos o privados, y la versi贸n gratuita de Codespaces permite disfrutar de 60 horas al mes de entorno de desarrollo en la nube desde cualquier navegador web. Esto es ideal para cualquiera que se quiera introducir al mundo del desarrollo y no quiera/pueda instalar nada en el dispositivo que va a utilizar.

De forma resumida, los pasos a seguir ser谩n:
1. Crear una cuenta en [Github](https://github.com)
2. Crear un [repositorio](https://docs.github.com/es/get-started/quickstart/create-a-repo) en Github.
3. Crear un [Codespace](https://docs.github.com/es/codespaces/developing-in-codespaces/creating-a-codespace-for-a-repository) a partir del repositorio.
4. Comenzar a desarrollar.

M谩s detalles en la [siguiente](02/02_Repo_Codespaces.md) lecci贸n.

> 馃摑 **Nota 1**:
> Antes de cerrar el navegador no olvides sincronizar los cambios con el repositorio de Github desde Visual Studio Code.

> 馃摑 **Nota 2**:
> Al finalizar cada sesi贸n de trabajo, elimina o para tu Codespace para no alcanzar el l铆mite de 60 horas gratuitas cuando no est谩s trabajando con el.

## Jupyter Notebooks 
[Jupyter Notebook](https://jupyter.org/) es un entorno web interactivo de programaci贸n dise帽ado en forma de cuaderno de notas. Es ampliamente utilizado en el ambito cient铆fico y de la ciencia de datos, por la sencillez y la facilidad para compartir desarrollos y algoritmos. Cada notebook contiene una o m谩s celdas consecutivas que pueden ser de texto en formato Markdown, utilizadas para proporcionar informaci贸n de contexto o dar instrucciones, o celdas de c贸digo en Python que pueden ejecutarse en un kernel de python dentro de Jupyter.

Al ser un entorno web es f谩cil empezar a trabajar con un notebook en python desde un simple navegador web. Por ejemplo, [aqu铆]((https://mybinder.org/v2/gh/ipython/ipython-in-depth/HEAD?urlpath=tree/binder/Index.ipynb)) puedes ver e interactuar con un notebook de Jupyter que contiene varios tutoriales de Jupyter.

Al ser un entorno web para trabajar con Jupyter Notebooks es necesario instalar un servidor Jupyter. Hay varias opciones:
 - [Instalar](https://jupyter.org/install) Jupyter en un equipo local.
 - Utilizar servidor Jupyter en internet como [Google Colab](https://colab.research.google.com/) o [Binder](https://mybinder.org/).


## Recursos de aprendizaje

- [Tutorial oficial de Python](https://docs.python.org/es/3/tutorial/).
- Repo [Cursos de Python desde cero](https://github.com/mouredev/Hello-Python) de Mouredev. Repositorios en Github + V铆deos.
- Repo [30 d铆as de Python](https://github.com/Asabeneh/30-Days-Of-Python).
- [Python for Everybody](https://www.py4e.com/)

**[Siguiente](../02/02_Repo_Codespaces.md)**