# 📗 Lección 05: Operadores

**[Índice](../README.md)**

**[Anterior](../05/05_Operadores.md)**

## Definición de Strings - Cadenas de texto

Las cadenas de texto se representan en python con objetos _str_. Se pueden definir entre comillas dobles o comillas sencillas, es inditinto.

Ejemplos:

```python
mi_cadena = "Esto es una cadena de texto"
otra_cadena = 'Esto es otra cadena de texto'
```

También se pueden definir entre triples comillas (dobles o sencillas) para textos multilínea.

Ejemplos:

```python
mi_cadena_multi = """Esto es una
cadena de texto"""
otra_cadena_multi = '''Esto es otra
cadena de texto'''
```

Se puede imprimir el contenido de una cadena de texto o imprimir la logitud de la cadena de texto.

Ejemplos:

```python
print(mi_cadena)
print(otra_cadena)
print(mi_cadena_multi)
print(otra_cadena_multi)
```

## Concatenación de cadenas de texto

Las cadenas de texto se pueden concatenar con el operador +. Otros operadores también pueden aplicarse a cadenas de texto.

Ejemplos:

```python
concatenada = mi_cadena + ' ' + otra_cadena
print(concatenada)
```

## Carácteres especiales

Las cadena pueden incluir caracteres especiales. Por ejmplo, _salto de línea_ (\n), _retorno de carro_ (\r) y _tabulación_ (\t).

💡 La barra invertida \ indica que el siguiente caracter es uno especial. Si se quiere utilizar una \ en el texto será necesario incluir dos barras invertidas \\.

Ejemplos:

```python
cadena_salto_linea = "Cadena con salto \n de línea"
cadena_tabulada = "\tCadena tabulada"
print(cadena_salto_linea)
print(cadena_tabulada)

cadena_escapada = "\\Esto es una cadena con barras invertidas \\"
print(cadena_escapada)

```

## Comparación

Comparan dos operandos. Los operadores de comparación son:

```
>       <       ==      >=      <=      !=
```

Ejemplos:

```python
# Comparación entre números
print(5>3)
print(5<3)
print(5==5)
print(5==6)
print(5!=6)

# Comparación de cadenas de texto
print("hola"=="Hola")
print("abanico"<"besugo")
```

## Lógicos

Se utilizan fundamentalmente para tomar una decisión en base a varias condiciones.

```
and     or      not
```

Ejemplos:

```python
print(True and False) # False
print(False or True) # True
print(not False) # True
print((3>2) and (5>1)) # True
```

## Operadores "is" e "in"

El operador _is_ devuelve _True_ si ambos operandos son el mismo objeto.

> 📝 **Nota:**
> Los operadores is y == no deben confundirse. Mientras el primero es para comprobar si dos operandos son el mismo objeto, el segundo es para comporar si tienen el mismo valor.

El operador _in_ sirve para comprobar si un operando está en una secuencia (cadenas, lista, tuplas).

```python
a = 3
b = a
print(a is b)

cadena = "mi cadena"
print("mi" in cadena)
print("no" in cadena)
```

**[Siguiente]()**
