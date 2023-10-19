# 📗 Lección 16: Ficheros

**[Índice](../README.md)**

**[Anterior](../15_EntornosVirtuales/README.md)**

## Ficheros

El manejo de archivos es una parte importante de la programación que nos permite crear, leer, actualizar y borrar archivos. En Python para manejar datos utilizamos la función incorporada *open()*.

```python
# sintaxis
open('fichero', modo) # modos(r, a, w, x, t, b)  could be to read, write, update
```

- "r" - Lectura - Valor por defecto. Abre un archivo para leerlo, devuelve un error si el archivo no existe
- "a" - Append - Abre un fichero para añadir, crea el fichero si no existe.
- "w" - Write - Abre un archivo para escritura, crea el archivo si no existe.
- "x" - Create - Crea el fichero especificado, devuelve un error si el fichero existe
- "t" - Texto - Valor por defecto. Modo texto
- "b" - Binary - Modo binario (por ejemplo, imágenes)

## Apertura de ficheros para lectura

El modo por defecto de *open* es lectura y texto, por lo que no es necesario especificar el modo *'r'* o *'rt'*.

```python
f = open('./ejemplo.txt')
print(f) # No imprime el contenido del archivo, sino otra información
print(type(f))
f.close()
```

El archivo abierto tiene diferentes métodos de lectura: *read()*, *readline*, *readlines*. Un archivo abierto tiene que ser cerrado con el método *close()*.

- *read()*: lee todo el texto como cadena. Si queremos limitar el número de caracteres que queremos leer, podemos limitarlo pasando un valor int al método *read(number)*.

```python
f = open('./ejemplo.txt')
print(f) # No imprime el contenido del archivo, sino otra información
print(type(f))
texto = f.read()
print(type(texto))
print(texto)
f.close()
```

- *readline()*: Lee únicamente la primera línea, en sucesivas llamadas irá leyendo la siguiente línea.

```python
f = open('./ejemplo.txt')
print(f) # No imprime el contenido del archivo, sino otra información
print(type(f))
linea = f.readline()
print(type(linea))
print(linea)
linea = f.readline()
print(type(linea))
print(linea)
f.close()
```

- *readlines()*: Lee todo el téxto línea a línea, y devuelve un diccionario de líneas.

```python
f = open('./ejemplo.txt')
print(f) # No imprime el contenido del archivo, sino otra información
print(type(f))
lineas = f.readlines()
print(type(lineas))
for i,linea in enumerate(lineas):
    print(f'Línea {i}: {linea}')
f.close()
```

Ejemplo con archivo csv:

```python
f = open('./ejemplo.csv')
print(f) # No imprime el contenido del archivo, sino otra información
print(type(f))
lineas = f.readlines()
print(type(lineas))
for i,linea in enumerate(lineas):
    print(f'Línea {i}: {linea}')
f.close()
```

Después de abrir un archivo, debemos cerrarlo. Hay una gran tendencia a olvidarse de cerrarlos. Con *with* - cierra los archivos por sí mismo. El ejemplo anterior con *with* sería:

```python
with open('./ejemplo.csv') as f:
    print(f) # No imprime el contenido del archivo, sino otra información
    print(type(f))
    lineas = f.readlines()
    print(type(lineas))
    for i,linea in enumerate(lineas):
        print(f'Línea {i}: {linea}')
print('Al salir del with se ha cerrado el archivo')
```

## Apertura de ficheros para escritura

Para escribir en un archivo hay que indicar el modo *a* o *w* en la función *open()*:

- "a" - append - añadir al final de un archivo, si no exite lo crea.
- "w" - write - sobreescribe un archvo existente, si no existe lo crea.

Ejemplo:

```python
with open('.ejemplo.txt','a') as f:
    f.write('Texto añadido al final')
```

El siguiente ejemplo sobreescribirá el contenido del archivo si existe, si no existe lo creará:

```python
with open('./ejemplo2.txt','w') as f:
    f.write('This text will be written in a newly created file')
```

## Borrando ficheros

El módulo *os* proporciona métodos para borrar archivos.

```python
import os
os.remove('./ejemplo2.txt)
```

Si el archivo no existe, el módulo *os* dará un error, así que es buena idea comprobar primero si lo que vamos a borrar existe:

```python
import os
if os.path.exists('./ejemplo2.txt'):
    os.remove('./ejemplo2.txt')
else:
    print('El fichero no existe')
```

Otra opción:

```python
import os
try:
    os.remove('./ejemplo2.txt')
except FileNotFoundError as e:
    print(e)
```




**[Siguiente](../17_HTTP/README.md)**
