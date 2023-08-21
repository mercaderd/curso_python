# Lección 06: Strings - Cadenas de texto

# Aritméticos
print(2+2)
print(2*2)
print(2**4)

# Operadores aritméticos con cadenas
print("cadena" * 3) # Devuelve la cadena repetida 3 veces
print("cadena1" + "cadena2") # El operador + concatena cadenas

# Operadores de asignación
a = 5
a += 3 # a = a + 3
a *= 2 # a = a * 2
print(a) # 16

# Operadores de comparación
# Comparación entre números
print(5>3)
print(5<3)
print(5==5)
print(5==6)
print(5!=6)

# Comparación de cadenas de texto
print("hola"=="Hola")
print("abanico"<"besugo")

# Operadores lógicos
print(True and False) # False
print(False or True) # True
print(not False) # True
print((3>2) and (5>1)) # True

# Operadores is e in
a = 3
b = a
print(a is b)

cadena = "mi cadena"
print("mi" in cadena)
print("no" in cadena)