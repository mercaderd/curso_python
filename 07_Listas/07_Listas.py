# Lección 07: Listas

# Creación de listas vacías

mi_lista = [] # Esto es una lista vacía
mi_otra_lista = list() # Esto es otra lista vacía

print(mi_lista)
print(mi_otra_lista)

print(type(mi_lista))
print(type(mi_otra_lista))

# Creación de listas con valores iniciales

mi_lista = [3,4,5,6, 6, 6, 6] # Pueden tener elementos repetidos
mi_otra_lista = ["queso", "plátano", "🎈", 35, 44, 2.2, None, "uno"] # Puenden contener elementos de distinto tipo

print(mi_lista)
print(mi_otra_lista)

print(type(mi_lista))
print(type(mi_otra_lista))

# Número de elementos de una lista

print("Lista:", mi_lista)
print(f"Número de elementos: {len(mi_lista)}")

print("Lista:", mi_otra_lista)
print(f"Número de elementos: {len(mi_otra_lista)}")

# Accediendo a los elementos de una lista

primer_elemento = mi_lista[0]
ultimo_elemento = mi_lista[-1] # Se pueden utilizar índices negativos

print(f"Lista: {mi_lista}")
print(f"El primer elemento de la lista es {primer_elemento}")
print(f"El último elemento de la lista es {ultimo_elemento}")

tercer_elemento = mi_otra_lista[2]

print(f"Lista: {mi_otra_lista}")
print(f"El tercer elemento de la lista es {tercer_elemento}")

# Desempaquetando elementos de una lista
print(f"Lista inicial: {mi_otra_lista}")
primero, segundo, tercero, cuarto, quinto, sexto, septimo, octavo = mi_otra_lista
print(f"El tercer elemento de la lista es {tercero}")

# Cambiando elementos de una lista

mi_otra_lista[2]="globo"
print(f"Lista cambiada: {mi_otra_lista}")
primero, segundo, tercero, cuarto, quinto, sexto, septimo, octavo = mi_otra_lista
print(f"El tercer elemento de la lista es {tercero}")

# Accediendo a partes de una lista - Slicing

print(f"La lista completa es: {mi_otra_lista}")

print(f"Dos primeros elementos: {mi_otra_lista[:2]}") 
print(f"Todos los elementos desde el tercero hasta el final: {mi_otra_lista[2:]}")
print(f"Uno de cada dos elementos desde el primero: {mi_otra_lista[::2]}")
print(f"Lista invertida: {mi_otra_lista[::-1]}")

# Se puede cambiar una parte de la lista
mi_otra_lista[:2] = ["uno", "dos"]
print(f"La lista modificada es: {mi_otra_lista}")

# Comprobando si un elemento está en la lista

globo_en_lista = "globo" in mi_otra_lista
print(globo_en_lista)

none_en_lista = None in mi_otra_lista
print(none_en_lista)

num_en_lista = 35 in mi_otra_lista
print(num_en_lista)

num_en_lista = 2.2 in mi_otra_lista
print(num_en_lista)

cabra_en_lista = "cabra" in mi_otra_lista
print(cabra_en_lista)

# Concatenar listas

mi_lista_completa = mi_lista + mi_otra_lista

print(f"Mi lista completa es: {mi_lista_completa}")

# Añadir elementos a una lista

print(f"Mi lista: {mi_lista}")
mi_lista.append("hola")
print(f"Mi lista con elemento añadido: {mi_lista}")

# Una lista puede tener como elementos otras listas

mi_lista.append(["elemento1", "elemento2"])
print(f"Mi lista con elemento añadido: {mi_lista}")

print(f"Mi lista con elemento añadido: {mi_lista}")

# Eliminar elementos de una lista

print(f"Mi lista: {mi_lista_completa}")
mi_lista_completa.remove("dos")
print(f"Mi lista: {mi_lista_completa}")
mi_lista_completa.remove("uno") # Si hay varios elementos iguales, elimina el primero de ellos.
print(f"Mi lista: {mi_lista_completa}")

mi_lista_completa.pop() 
print(f"Mi lista: {mi_lista_completa}")

elemento = mi_lista_completa.pop(7) 
print(f"Mi lista: {mi_lista_completa}. Se ha eliminado el elemento: {elemento}")

mi_lista_completa.clear() 
print(f"Mi lista: {mi_lista_completa}")