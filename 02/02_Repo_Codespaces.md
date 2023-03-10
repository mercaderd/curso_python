# 馃摋 Lecci贸n 02: Hola Mundo con Github y Codespaces

**[脥ndice](../README.md)**

**[Anterior](../01/01_Introduccion.md)**

## Pasos previos
Para continuar con esta lecci贸n, previamente deber铆as:
- Haber creado una cuenta (gratuita) de usuario en [Github](https://github.com).
- Haber iniciado sesi贸n en [Github](https://github.com) con esa cuenta de usuario.

## Crear un repositorio en Github para desarrollar en Python

Un repositorio(repo) en Github es un espacio de almacenamiento en el que alojar el c贸digo fuente de un proyecto y otros archivos importantes para el proyecto. Tienes informaci贸n completa sobre repositorios de Github [aqu铆](https://docs.github.com/es/repositories/creating-and-managing-repositories/about-repositories).

1. Para crear un nuevo repositorio pulsa el signo + en la parte superior derecha de la pantalla y selecciona "New repository".

![Nuevo repo](./media/001_NewRepo.jpg)

2. Asigna un nombre a tu repositorio y opcionalmente una descripci贸n. Marca la opci贸n "Add a README file", elije un template de Python para a帽adir un archivo .gitignore y selecciona la licencia que prefieras para tu repositorio. Finalmente, pulsa "Create Repository".

![Datos del repo 1](./media/002_NewRepo.jpg)
![Datos del repo 2](./media/003_NewRepo.jpg)

Con estos sencillo pasos, habr谩s creado un nuevo repositorio. En la parte central se muestra la lista de archivos que contiene el repositorio inicialmente. En la parte inferior se muestra una previsualizaci贸n del archivo README.md (markdown) y en la parte derecha se muestra informaci贸n sobre el respositorio (puede editarse en cualquier momento.)

![Repo reci茅n creado](./media/004_NewRepo.jpg)

## Crear un Codespace con Python + Visual Studio Code para comezar a desarrollar

Con una cuenta gratuita de Github dispondr谩s de 60 horas al mes de Codespaces. Consulta informaci贸n completa sobre Github Codespaces [aqu铆](https://docs.github.com/es/codespaces/overview).

3. Pulsa el bot贸n "Code" (parte superior derecha de la vista del repositorio). Selecciona la pesta帽a "Codespaces" y pulsa el bot贸n "Create codespace on main".

![Create codespace](./media/005_NewRepo.jpg)

Pasados unos segundos, dispondr谩s de un entorno de desarrollo completo para Python 3 con Visual Studio Code. Puedes cambiar los colores (el tema) de Visual Studio Code, para tener el fondo negro y texto coloreado.

4. (Opcional) Pulsa la rueda dentada (bot贸n ajustes) de la parte inferior izquierda de la ventana. Selecciona "Tema de color" y elije el tema que m谩s te guste. En mi caso, "Github Dark".

![Ajustes Visual Studio Code](./media/006_NewRepo.jpg)

5. En la parte izquierda de la pantalla de Visual Studio Code se muestra la lista de archivos del repositorio. Haz doble click sobre README.md y modif铆calo seg煤n se muestra en la siguiente im谩gen. Sobre el bot贸n de control de versiones de la parte izquierda aparecer谩 una bolita azul con el n煤mero 1 (significa que hay cambios en un archivo, el que acabas de modificar).

![README.md](./media/007_NewRepo.jpg)

## Hola Mundo en Python

Los scripts o programas en Python se escriben en archivos de texto con extensi贸n ".py".

6. En la parte izquierda de la pantalla, junto al nombre del repositorio, pulsa el bot贸n "Nuevo archivo..." y crea un archivo llamado "main.py".

![Nuevo archivo](./media/008_NewRepo.jpg)

7. Completa el archivo "main.py" con el texto "print("隆Hola mundo!")", tal y c贸mo se muestra en la im谩gen.

```python
print("隆Hola mundo!")
```

![main.py](./media/009_NewRepo.jpg)

Este programa es muy sencillo, 煤nicamente escribe por pantalla/consola el mensaje "隆Hola Mundo!" cada vez que se ejecuta.

Visual Studio Code detectar谩 que est谩s desarrollando en Python y te preguntar谩 si quieres instalar la extensi贸n de Python para Visual Studio Code. Es muy recomendable responder que s铆.

![Extensi贸n Python](./media/010_NewRepo.jpg)

8. Ejecuta el script pulsando el bot贸n 鈻? de la parte superior derecha de la pantalla. Visual Studio Code abrir谩 un terminal de Python en la parte inferior de la pantalla y ejecutar谩 el script. Si no hay ning煤n problema, imprimir谩 el mensaje "隆Hola mundo!".

![Git](./media/011_NewRepo.jpg)

9. (Opcional) Prueba a cambiar el texto entre comillas 隆Hola mundo! por cualquier otro mensaje y ejecuta de nuevo el script.

```python
print("驴Qu茅 miras?, Bobo")
```

## Sincronizar los cambios con el repositorio de Github

Consulta informaci贸n b谩sica sobre el control de versiones git y Github [aqu铆](https://docs.github.com/es/get-started/using-git/about-git).

Desde Visual Studio Code es posible trabajar con el control de versiones Git y mantener el respositorio sincronizado con Github. Para ello, es necesario ir a la pesta帽a de control de versiones.

10. En los botones de la izquierda, pulsa en de control de versiones (marcado en rojo en la siguiente im谩gen).

![Git](./media/013_NewRepo.jpg)

En el panel de la izquierda se pueden comprobar qu茅 archivos tienen cambios, en este caso dos archivos.

11. Confirma los cambios que quieres hacer en el repositorio, en este caso los cambios en todos los archivos. Pulsa el + que se marca en rojo en la siguiente im谩gen. (Tambi茅n podr铆as confirmar los cambios de forma individual en cada archivo, pulsando el bot贸n + en cada uno de ellos.)

![Git](./media/014_NewRepo.jpg)

12. Haz "commit" en el respositorio en local (d贸nde est茅s trabajando con VSCode, tu ordenador o un Codespace). Escribe un mensaje descriptivo en el cuadro de texto y pulsa el bot贸n "Confirmaci贸n".

![Git](./media/015_NewRepo.jpg)

13. Sincroniza los cambios con el repositorio en Github pulsando el bot贸n "Sincronizar cambios".

![Git](./media/016_NewRepo.jpg)

Aparecer谩 el siguiente mensaje que debes aceptar o marcar "Ok, Don't show again".

![Git](./media/017_NewRepo.jpg)

Tambi茅n puede aparecerte el siguiente mensaje para que el codespace se actualice regularmente con el repositorio. Pulsa igualmente "S铆".

![Git](./media/018_NewRepo.jpg)

Tras unos instantes, todos los cambios se habr谩n sincronizado con el repositorio en GitHub. Si visitas tu repositorio (es posible que tengas que refrescar el navegador) en Github, ver谩s que todos los cambios se han aplicado.

![Git](./media/019_NewRepo.jpg)

## Cerrar el Codespace

Cuando acabes de desarrollar es necesario cerrar el codespace para que no permanezca activo. Mientras el codespace est谩 desactivado no computar谩n las horas de uso. Recuerda que para una cuenta gratuita de Github el l铆mite son 60h/mes gratis, a partir de la hora 60 tiene un coste. Cada mes se resetean las 60 horas gratuitas.

14. Para cerrar el codespace pulsa sobre "Codespaces" en la parte inferior izquierda de la ventana de Visual Studio Code, y pulsa "Stop Current Codespace" entre las opciones disponibles.

![Git](./media/020_NewRepo.jpg)

Para volver a trabajar con Visual Studio Code tendr谩s que volver a lanzar el Codespace. No hay limitaci贸n en cuanto al n煤mero de veces que puede pararse o lanzarse un Codespace.

## Rearrancar un Codespace

15. Desde Github, con la sesi贸n iniciada pulsa "Codespaces" en la barra superior.

![Git](./media/021_NewRepo.jpg)

16. Pulsa sobre el nombre del codespace que quieres rearrancar y confirma pulsando el bot贸n "Restart codespace".

![Git](./media/022_NewRepo.jpg)

![Git](./media/023_NewRepo.jpg)

En unos segundos volver谩s a tener Visual Studio Code listo para continuar trabajando.

**[Siguiente](../03/03_Lexico.md)**

