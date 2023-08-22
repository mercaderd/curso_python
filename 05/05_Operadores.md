# 📗 Lección 05: Operadores

**[Índice](../README.md)**

**[Anterior](../04/04_Variables.md)**

## Aritméticos

Los operadores aritméticos toman dos operandos y devuelven un resultado.
```
+       -       *       /       %       **      //
```
Ejemplos:
```python
print(2+2)
print(2*2)
print(2**4)
```
Algunos operadores aritméticos también funcionan con cadenas de texto:
```python
print("cadena" * 3) # Devuelve la cadena repetida 3 veces
print("cadena1" + "cadena2") # El operador + concatena cadenas
```

## Asignación

Se utilizan para asignar un valor a una variable. El principal operador de asignación es el símbolo igual (=).

Otros operadores de asignación son:
```
=       +=      -=      *=      /=      %=
**=     //=     &=      |=      ^=      >>=
<<=
```

Ejemplos típicos:
```python
a = 5
a += 3 # a = a + 3
a *= 2 # a = a * 2
print(a) # 16
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

El operador *is* devuelve *True* si ambos operandos son el mismo objeto.

> 📝 **Nota:**
> Los operadores is y == no deben confundirse. Mientras el primero es para comprobar si dos operandos son el mismo objeto, el segundo es para comporar si tienen el mismo valor.

El operador *in* sirve para comprobar si un operando está en una secuencia (cadenas, lista, tuplas).

```python
a = 3
b = a
print(a is b)

cadena = "mi cadena"
print("mi" in cadena)
print("no" in cadena)
```

**[Siguiente](../06/06_Strings.md)**

