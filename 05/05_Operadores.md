# 馃摋 Lecci贸n 05: Operadores

**[脥ndice](../README.md)**

**[Anterior](../04/04_Variables.md)**

## Aritm茅ticos

Los operadores aritm茅ticos toman dos operandos y devuelven un resultado.
```
+       -       *       /       %       **      //
```
Ejemplos:
```python
print(2+2)
print(2*2)
print(2**4)
```
Algunos operadores aritm茅ticos tambi茅n funcionan con cadenas de texto:
```python
print("cadena" * 3) # Devuelve la cadena repetida 3 veces
print("cadena1" + "cadena2") # El operador + concatena cadenas
```

## Asignaci贸n

Se utilizan para asignar un valor a una variable. El principal operador de asignaci贸n es el s铆mbolo igual (=).

Otros operadores de asignaci贸n son:
```
=       +=      -=      *=      /=      %=
**=     //=     &=      |=      ^=      >>=
<<=
```

Ejemplos t铆picos:
```python
a = 5
a += 3 # a = a + 3
a *= 2 # a = a * 2
print(a) # 16
```

## Comparaci贸n

Comparan dos operandos. Los operadores de comparaci贸n son:
```
>       <       ==      >=      <=      !=
```

Ejemplos:
```python
# Comparaci贸n entre n煤meros
print(5>3)
print(5<3)
print(5==5)
print(5==6)
print(5!=6)

# Comparaci贸n de cadenas de texto
print("hola"=="Hola")
print("abanico"<"besugo")
```

## L贸gicos

Se utilizan fundamentalmente para tomar una decisi贸n en base a varias condiciones.

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

> 馃摑 **Nota:**
> Los operadores is y == no deben confundirse. Mientras el primero es para comprobar si dos operandos son el mismo objeto, el segundo es para comporar si tienen el mismo valor.

El operador *in* sirve para comprobar si un operando est谩 en una secuencia (cadenas, lista, tuplas).

```python
a = 3
b = a
print(a is b)

cadena = "mi cadena"
print("mi" in cadena)
print("no" in cadena)
```

**[Siguiente]()**

