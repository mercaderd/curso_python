# 📗 Lección 06: Strings - Cadenas de caracteres

**[Índice](../README.md)**

**[Anterior](../05_Operadores/README.md)**

## Definición

Las cadenas de caracteres se representan en python con objetos *str*. Se pueden definir entre comillas dobles o comillas sencillas, es inditinto.

```python
# Definición de cadenas de caracteres (strings)
mi_cadena = "Esto es una cadena de texto"
otra_cadena = 'Esto es otra cadena de texto'
```

También se pueden definir entre triples comillas (dobles o sencillas) para textos multilínea.

```python
# Definición de cadenas multilínea
mi_cadena_multi = """Esto es una 
cadena de texto multilínea"""
otra_cadena_multi = '''Esto es otra 
cadena de texto multilínea'''
```

Se puede imprimir el contenido de una cadena de caracteres o imprimir la logitud de la cadena de texto.

```python
# Imprimir cadenas de caracteres
print(mi_cadena)
print(otra_cadena)
print(mi_cadena_multi)
print(otra_cadena_multi)

# Imprimir la longitud de cadenas de caracteres
print(len(mi_cadena))
print(len(mi_cadena_multi))
```

Una cadena de texto puede contener números, pero sigue siendo una cadena de texto. Una cadena de texto que contiene números puede ser convertida a una variable de tipo entero con *int()*. Un número entero puede ser convertido a cadena de texto con *str()*.

```python
# Esto es una cadena de caracteres que contiene números
asistentes = "995"
print(type(asistentes))
print(asistentes)
asistentes_int = int(asistentes)
print(type(asistentes_int))
print(str(asistentes_int))
```

Se puede pedir al usuario que introduzca datos con *input()*, que los leerá siempre como string. Luego se pueden convertir al tipo de variable más conveniente.

```python
# Leer datos del usuario y convertir al tipo de variable necesario
n1 = input("Introduzca su nota en matemáticas: ")
n2 = input("Introduzca su nota en lengua: ")
media = (float(n1) + float(n2)) / 2
print("Su nota media es: " + str(media))
```

## Concatenación de cadenas de caracteres

Las cadenas de caracteres se pueden concatenar con el operador +. Otros operadores también pueden aplicarse a cadenas de caracteres.

```python
# Concatenar cadenas de caracteres
concatenada = mi_cadena + '  🎉 CONCATENADA CON  🎉 ' + otra_cadena
print(concatenada)

# Algunas variables se pueden convertir a cadena de caracteres con str(variable) y concatenar con otras cadenas de caracteres
print("La cadena de texto '" + mi_cadena +"' tiene una longitud de " + str(len(mi_cadena)) + " caracteres")
```

## Carácteres especiales

Las cadenas pueden incluir caracteres especiales. Por ejmplo, _salto de línea_ (\n), _retorno de carro_ (\r) y _tabulación_ (\t).

💡 La barra invertida \ indica que el siguiente caracter es uno especial. Si se quiere utilizar una \ en el texto será necesario incluir dos barras invertidas \\.

Ejemplos:

```python
# Caracteres especiales
cadena_salto_linea = "Cadena con salto \n de línea"
cadena_tabulada = "\tCadena tabulada"
print(cadena_salto_linea)
print(cadena_tabulada)

cadena_escapada = "\\Esto es una cadena con barras invertidas\\"
print(cadena_escapada)

otro_ejemplo = "\n" + "Primera línea" + "\n" + "\tSegunda línea tabulada"
print(otro_ejemplo)
```

## Imprimir cadenas con formato (combinando otras variables)

Aunque es posible concatenar cadenas, el objeto str tiene opciones para formatear cadenas de texto. Se puede utilizar el método *format*, el operador *%* o f-strings.

Ejemplos:

```python
# Imprimir cadenas de texto con formato
nombre, apellido, edad = "Bob", "El Silencioso", 29
print("Me llamo {} {} y mi edad es {} años".format(nombre, apellido, edad))
print("Me llamo %s %s y mi edad es %d años" % (nombre, apellido, edad))

# Formateo avanzado con f-strings
print(f"Me llamo {nombre} {apellido} y mi edad es {edad} años")

num = 87
print(f"¿num es par? {True if num%2==0 else False}")
```

## Acceso a elementos internos de las cardenas

- Se puede acceder a los caracteres individuales de una cadena utilizando un índice entre corchetes. Ej: cadena[3]
- El índice debe ser un entero, comenzando por cero (primer caracter).
- Se pueden especificar índices negativos y se comienza a contar desde el final de la cadena, Ej: *-1* será el índice del último caracter.

```python
#Acceso a elementos internos mediante índice
print(mi_cadena)
print(mi_cadena[0]) # Acceso al primer caracter
print(mi_cadena[3]) # Acceso al cuarto caracter

# Índices negativos, -1 último caracter, -2 penúltimo, ...
print(mi_cadena[-1])
print(mi_cadena[-2])

# Utilizar un índice mayor que la longitud de la cadena provoca un error
print(mi_cadena[100]) # ¡Ojo! ¡Esto de error!
```

- Los índices pueden ser el resultado de una expresión.

```python
# Se puende utilizar expresiones para indicar los índices, por ejemplo a partir de len()
print(mi_cadena)
print(mi_cadena[len(mi_cadena) - 1])
```

## Subcadenas o slices

- También se puede acceder a partes de una cadena de texto (slices). Entre corchetes se indica el índice inicial y el índice final separados por *:*. Ejemplo: mi_cadena[2:5]
- Incluye todos los caracteres del índice inicial al final (sin incluir el final). 
- Si se deja en blanco el índice inicial, se considera el inicio de la cadena.
- Si se deja en blanco el índie final, se considera el final de la cadena.
- Si se dejan ambos en blanco, se considera la cadena completa.

```python
# Subcadenas o Slices
print(mi_cadena)
print(mi_cadena[5:14])
print(mi_cadena[:10])
print(mi_cadena[10:])
print(mi_cadena[:])
```

- Se pueden especificar índices negativos y se comienza a contar desde el final de la cadena, Ej: *-1* será el índice del último caracter.

```python
# Indicando números negativos el índice comienza a contar desde el final de la cadena. Ej: -1 será el índice del último caracter.
print(mi_cadena[10:-1])
```

- Un tercer índice se puede especificar para indicar saltos en la selección de caracteres o que se recorra en orden inverso.

```python
# Seleccionar uno de cada dos caracteres entre el rango especificado
print(mi_cadena[2:10:2])

# Especificar orden invertido con *-1* como tercer índice.
print(mi_cadena[::-1])
print(mi_cadena[:10:-1])
```

## Métodos de las cadenas de caracteres

Los objetos cadena de texto tienen métodos muy útiles. Están disponibles para cualquier cadena. 

👁‍🗨 **No modifican la cadena original, devuelven una nueva cadena.**

- **.capitalize()**: Retorna una copia de la cadena con el primer carácter en mayúsculas y el resto en minúsculas. 
- **.upper()**: Devuelve copia de la cadena con todos los caracteres en mayúscula. (Si tienen forma mayúscula)
- **.count(sub[,start[, end]])**: Devuelve el número de ocurrencias no solapadas de la cadena sub en el rango [start, end]. Los parámetros opcionales start y end Se interpretan como en una expresión de rebanada.
- **.isnumeric()**: Retorna True si todos los caracteres de la cadena son caracteres numéricos y hay, al menos, un carácter. En caso contrario, retorna False.
- **.lower()**: Retorna una copia de la cadena de caracteres con todas las letras en minúsculas
- **.startswith(prefix[, start[, end]])**: Retorna True si la cadena empieza por prefix, en caso contrario Retorna False.
- **.strip([chars])**: Retorna una copia de la cadena con los caracteres indicados eliminados, tanto si están al principio como al final de la cadena. El parámetro chars especifica el conjunto de caracteres a eliminar. Si se omite o si se especifica None, se eliminan todos los espacios en blanco.
- **.rstrip([chars])**: Retorna una copia de la cadena, eliminado determinados caracteres si se encuentren al final. El parámetro chars especifica el conjunto de caracteres a eliminar. Si se omite o si se especifica None, se eliminan todos los espacios en blanco.
- **.lstrip([chars])**: Igual que la anterior pero si los caracteres al principio.
- **.split(sep=None, maxsplit=- 1)**: Retorna una lista con las palabras que componen la cadena de caracteres original, usando como separador el valor de sep.
- **.replace(old, new[, count])**: Retorna una copia de la cadena con todas las ocurrencias de la cadena old sustituidas por new. Si se utiliza el parámetro count, solo se cambian las primeras count ocurrencias.
- **.find(sub[, start[, end]])**: Retorna el menor índice de la cadena s donde se puede encontrar la cadena sub, considerando solo el intervalo s[start:end]. Los parámetros opcionales start y end se interpretan como si fueran “indices de una rebanada. retorna -1 si no se encuentra la cadena.

El resto se pueden consultar en la documentación o en la [ayuda](https://docs.python.org/es/3.10/library/stdtypes.html#string-methods) de Python.

```python
# Métodos de cadenas de caracteres

c1 = "esto es una cadena"
c2 = "123"
c3 = "id;username;passwd;email;address"
c4 = "EstohiEshiUnahiCadenahiDehiCaractereshiHipnótica"
c5 = "       ¿Cadena de Texto?        "

# Mayusculas y minúsculas
c1.capitalize()
print(c1) # c1 no ha sido modificada
cap1 = c1.capitalize()
print (cap1)
print(cap1.lower())
print("-------------")

upp1 = c1.upper()
print(upp1)
print(upp1.lower())
print("-------------")

# Contar ocurrencias
print(c3.count(';')) # Contar número de ; en c3
print(c1.count(' ')) # Contar número de espacios en blanco
print(c4.count('hi'))
print("-------------")

# Eliminar ocurrencias
print(c5.strip())
print(c5.strip(" ¿?"))
print("-------------")

# Encontrar ocurrencias
print(c4.find('hi'))
print(c4.find('hi',5))
print(c5.find('hi')) # Devuelve -1 si no hay ocurrencias
print("-------------")

# Reemplazar ocurrencias
print(c4.replace('hi',' '))
print('\n')
print(c3.replace(';','\n'))
print("-------------")

# Separar por delimitador
lista = c3.split(';')
print(lista)
for element in lista:
    print(element)
print("-------------")
```
**[Siguiente](../07_Bla/README.md)**
