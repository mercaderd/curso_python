# Lección 4: Variables

# Variables en Python
nombre = 'Daniel'
apellido = "García"
pais = 'España'
ciudad = 'Madrid'
edad = 45
casado = False

# Variables numéricas
entero = 5
con_decimales = 5.5 # Ojo, se utiliza . como separador decimal
complejo = 1 + 2j

# Imprimir los valores
print(entero)
print(con_decimales)
print(complejo)

# Declarar cadenas de texto
una_cadena = "Primera cadena de texto"
otra_cadena = 'Otra cadena de texto'
tercera_cadena = "Tercera 'cadena' de texto"

#Imprimir cadenas de texto
print(una_cadena)
print(otra_cadena)
print(tercera_cadena)

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

# Cambiar el tipo de una variable
edad = 30
print(type(edad))
# Asignamos una cadena de texto
edad = "treinta"
print(type(edad))

# Ejemplo casting de variables
un_numero = 3
otro_numero = "6" # Declarado como cadena de texto

suma = un_numero + int(otro_numero)

print(str(3),"+",otro_numero,"=",str(suma))