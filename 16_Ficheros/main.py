# Ficheros

import os
import json
import csv

# Abrir ficheros

f = open('./ejemplo.txt', encoding='utf-8')
print(f) # No imprime el contenido del archivo, sino otra información
print(type(f))
f.close()

# Leer un fichero de una vez

f = open('./ejemplo.txt', encoding='utf-8')
print(f) # No imprime el contenido del archivo, sino otra información
print(type(f))
texto = f.read()
print(type(texto))
print(texto)
f.close()


# Leer todas las líneas de una vez pero línea a línea.

f = open('./ejemplo.txt', encoding='utf-8')
print(f) # No imprime el contenido del archivo, sino otra información
print(type(f))
lineas = f.readlines()
print(type(lineas))
for i,linea in enumerate(lineas):
    print(f'Línea {i}: {linea}')
f.close()

# Otra posibilidad

f = open('./ejemplo.txt', encoding='utf-8')
print(f) # No imprime el contenido del archivo, sino otra información
print(type(f))
for linea in f: # Recorrer directamente el archivo como un iterable
    print(linea)
f.close()

# Ejemplo con fichero CSV

f = open('./ejemplo.csv', encoding='utf-8')
print(f) # No imprime el contenido del archivo, sino otra información
print(type(f))
lineas = f.readlines()
print(type(lineas))
for i,linea in enumerate(lineas):
    print(f"Línea {i}: {linea.split(sep = ',')}")
f.close()

# Utilizando with para no olvidar cerrar el fichero

with open('./ejemplo.csv', encoding='utf-8') as f:
    print(f) # No imprime el contenido del archivo, sino otra información
    print(type(f))
    lineas = f.readlines()
    print(type(lineas))
    for i,linea in enumerate(lineas):
        print(f"Línea {i}: {linea.split(sep = ',')}")
print('Al salir del with se ha cerrado el archivo')

# Apertura de ficheros para escritura

with open('./ejemplo.txt','a', encoding='utf-8') as f:
    f.write('Texto añadido al final')

with open('./ejemplo2.txt','w', encoding='utf-8') as f:
    f.write('Texto añadido en un archivo nuevo')


os.remove('./ejemplo2.txt')

if os.path.exists('./ejemplo2.txt'):
    os.remove('./ejemplo2.txt')
else:
    print('El fichero no existe')


try:
    os.remove('./ejemplo2.txt')
except FileNotFoundError as e:
    print(e)


persona = {
   'nombre':'Manuel',
   'apellido':'Ejemplar',
   'edad':26,
   'país':'España',
   'casado':True,
   'conocimientos':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
   'direccion':{
       'calle':'De la protección de datos',
       'cp':'28000'
   }
   }

persona_json = json.dumps(persona,
                          indent = 4,
                          ensure_ascii=False) # Convierte el diccionario en una cadena JSON
print(persona_json)

# Guardar el fichero JSON
with open('./persona.json', mode = 'w', encoding = 'utf-8') as f:
    f.write(persona_json)

# Otra forma más directa
with open('./persona.json', mode = 'w', encoding = 'utf-8') as f:
    json.dump(persona, f, ensure_ascii=False, indent=4)

# Leer un archivo JSON

with open('./persona.json', encoding='utf-8') as f:
    persona_json = f.read()

persona = json.loads(persona_json)

print(type(persona))

# Otra forma

with open('./persona.json', encoding='utf-8') as f:
    persona = json.load(f)

print(persona)

# Archivos CSV - Lectura

with open('./ejemplo.csv', encoding='utf-8') as f:
    lineas = csv.reader(f)
    for i,linea in enumerate(lineas):
        if i == 0:
            print(f'Columnas: {", ".join(linea)}')
        elif i < 10:
            print(f'Datos {i}: {", ".join(linea)}')


# Archivos CSV - Escritura

nombres_columnas = ["nombre", "apellido", "edad"]
linea1 = ["pedro", "moreno", "65"]
linea2 =["alberto", "garcia", "29"]
resto_de_lineas =[["nombre3", "apellido4", "edad4"],
                  ["nombre4", "apellido5", "edad5"],
                  ["nombre5", "apellido6", "edad6"]]

with open('./nuevocsv.csv', mode='w', encoding='utf-8') as f:
    csv_writer = csv.writer(f, delimiter=',')
    csv_writer.writerow(nombres_columnas)
    csv_writer.writerow(linea1)
    csv_writer.writerow(linea2)
    csv_writer.writerows(resto_de_lineas)
