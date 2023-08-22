# Lección 06: Strings - Cadenas de texto

# Definición de cadenas de caracteres (strings)
mi_cadena = "Esto es una cadena de texto"
otra_cadena = 'Esto es otra cadena de texto'

# Definición de cadenas multilínea
mi_cadena_multi = """Esto es una 
cadena de texto multilínea"""
otra_cadena_multi = '''Esto es otra 
cadena de texto multilínea'''

# Imprimir cadenas de caracteres
print(mi_cadena)
print(otra_cadena)
print(mi_cadena_multi)
print(otra_cadena_multi)

# Imprimir la longitud de cadenas de caracteres
print(len(mi_cadena))
print(len(mi_cadena_multi))

# Esto es una cadena de caracteres que contiene números
asistentes = "995"
print(type(asistentes))
print(asistentes)
asistentes_int = int(asistentes)
print(type(asistentes_int))
print(str(asistentes_int))

# Leer datos del usuario y convertir al tipo de variable necesario
n1 = input("Introduzca su nota en matemáticas: ")
n2 = input("Introduzca su nota en lengua: ")
media = (float(n1) + float(n2)) / 2
print("Su nota media es: " + str(media))

# Concatenar cadenas de caracteres
concatenada = mi_cadena + '  🎉 CONCATENADA CON  🎉 ' + otra_cadena
print(concatenada)

# Algunas variables se pueden convertir a cadena de caracteres con str(variable) y concatenar con otras cadenas de caracteres
print("La cadena de texto '" + mi_cadena +"' tiene una longitud de " + str(len(mi_cadena)) + " caracteres")

# Caracteres especiales
cadena_salto_linea = "Cadena con salto \n de línea"
cadena_tabulada = "\tCadena tabulada"
print(cadena_salto_linea)
print(cadena_tabulada)

cadena_escapada = "\\Esto es una cadena con barras invertidas\\"
print(cadena_escapada)

otro_ejemplo = "\n" + "Primera línea" + "\n" + "\tSegunda línea tabulada"
print(otro_ejemplo)

# Imprimir cadenas de texto con formato
nombre, apellido, edad = "Bob", "El Silencioso", 29
print("Me llamo {} {} y mi edad es {} años".format(nombre, apellido, edad))
print("Me llamo %s %s y mi edad es %d años" % (nombre, apellido, edad))

# Formateo avanzado con f-strings
print(f"Me llamo {nombre} {apellido} y mi edad es {edad} años")

num = 87
print(f"¿num es par? {True if num%2==0 else False}")

#Acceso a elementos internos mediante índice
print(mi_cadena)
print(mi_cadena[0]) # Acceso al primer caracter
print(mi_cadena[3]) # Acceso al cuarto caracter

# Utilizar un índice mayor que la longitud de la cadena provoca un error
# print(mi_cadena[100]) # ¡Ojo! ¡Esto de error!

# Se puende utilizar expresiones para indicar los índices, por ejemplo a partir de len()
print(mi_cadena)
print(mi_cadena[len(mi_cadena) - 1])

# Subcadenas o Slices
print(mi_cadena)
print(mi_cadena[5:14])
print(mi_cadena[:10])
print(mi_cadena[10:])
print(mi_cadena[:])

# Indicando números negativos el índice comienza a contar desde el final de la cadena. Ej: -1 será el índice del penúltimo caracter.
print(mi_cadena[10:-1])

# Seleccionar uno de cada dos caracteres entre el rango especificado
print(mi_cadena[2:10:2])

# Especificar orden invertido con *-1* como tercer índice.
print(mi_cadena[::-1])
print(mi_cadena[:10:-1])

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