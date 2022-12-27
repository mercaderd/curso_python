# Lección 04: Variables

**[Índice](../README.md)**

**[Anterior](../03/03_Lexico.md)**

Las variables sirven para guardar datos en memoria. Una variable es un espacio en memoria en el que almacenar distintos tipos de datos.

## Nombres de variables

Los nombres de variable pueden ser cortos o largos, pero se recomienda utilizar nombres descriptivos del contenido. 

En Pyhton deben cumplirse estas condiciones para los nombres de variables:
- Empezar por una letra o por guión bajo.
- No empezar por un número.
- Contener únicamente caracteres alfanuméricos o guión bajo (A-z,0-9,_).
- Se distingue entre mayúsculas y minúsculas (Name, NAME, NAme, name son variables distintas)

> **Nota:** La convención mas extendida en Python para los nombres de variables es utilizar *snake_case* (En otros lenguajes es habitual utilizar *Camel Case*). Snake case implica utilizar letras en minúsculas y separar palabras con guión bajo (_). 

Algunos ejemplos de nombres de variables en snake case son:
```
mi_variable
variable01
nombre
_if
codigo_postal
direccion
pais
direccion_postal
direccion_electronica
```

Las variables en Python se declaran asignándoles un valor, para lo que se utiliza el operador asignación (=). Algunos ejemplos:

```python
# Variables en Python
nombre = 'Daniel'
apellido = "García"
pais = 'España'
ciudad = 'Madrid'
edad = 45
casado = False
```

## Números

Las varibles numéricas pueden ser:
- Enteros
- Coma flotante (con decimales). Separador decimal: .
- Complejos

Declaración de variables numéricas:

```python
# Variables numéricas
entero = 5
con_decimales = 5.5 # Ojo, se utiliza . como separador decimal
complejo = 1 + 2j

# Imprimir los valores
print(entero)
print(con_decimales)
print(complejo)
```

## Cadenas de texto

Las cadenas de texto se pueden declarar indistintamente entre comillas dobles o comillas simples.
Ejemplos:

```python
# Declarar cadenas de texto
una_cadena = "Primera cadena de texto"
otra_cadena = 'Otra cadena de texto'
tercera_cadena = "Tercera 'cadena' de texto"

#Imprimir cadenas de texto
print(una_cadena)
print(otra_cadena)
print(tercera_cadena)
```
## Tipos de variables

Se puede comprobar el tipo de una variable utilizando la función *type()*, e imprimir el resultado con *print()*

Por ejemplo:
```python
# Comprobar el tipo de una variable
print(type(3))
print(type(3.14))
print(type(True))
print(type("cadena de texto"))
print(type(una_cadena))
print(type(entero))
print(type(con_decimales))
print(type(casado))


# Se pueden concatenar cadenas en un print
print("La variable una_cadena es de tipo: ", type(una_cadena))
```

Se puede cambiar el tipo de una varible asignándole un valor de otro tipo:

```python
# Cambiar el tipo de una variable
edad = 30
print(type(edad))
# Asignamos una cadena de texto
edad = "treinta"
print(type(edad))
```

También se puede forzar el cambio de tipo haciendo **Casting**. Se utilizan las funciones *int(), float(), str()*

```python
# Ejemplo casting de variables
un_numero = 3
otro_numero = "6" # Declarado como cadena de texto

suma = un_numero + int(otro_numero)

print(str(3),"+",otro_numero,"=",str(suma))
```

**[Siguiente]()**

