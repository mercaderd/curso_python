# Clases y objetos

# Creando una clase

class Persona():
    pass

print(Persona)

# Craeando un objeto

persona1 = Persona()
print(persona1)


# Constructor

class Persona():
    version = '1.0.0' # Atributo de clase
    def __init__(self, nombre, apellido = None, edad = None, pais = None, ciudad = None):
        self.nombre = nombre        # Atributos de objeto
        self.apellido = apellido
        self.edad = edad
        self.pais = pais
        self.ciudad = ciudad

persona1 = Persona("Pedro")
print(persona1)
print(persona1.nombre)
print(persona1.version)
persona2 = Persona("Alicia")
print(persona2)
print(persona2.nombre)
print(persona2.version)

# Métodos de objeto

class Persona():
    version = '1.0.0' # Atributo de clase
    def __init__(self, nombre, apellido = None, edad = None, pais = None, ciudad = None):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.pais = pais
        self.ciudad = ciudad
    def saluda(self):
        print(f"Hola, soy {self.nombre}. Encantado de saludarte.")
    def datos(self):
        return {
            'nombre': self.nombre,
            'apellido': self.apellido,
            'edad': self.edad,
            'pais': self.pais,
            'ciudad': self.ciudad
            }
    
persona1 = Persona("Pedro", apellido="Hernando", edad=54)
persona1.saluda()
print(persona1.datos())

## Método para modificar atributos de objeto

class Persona():
    version = '1.0.0' # Atributo de clase
    def __init__(self, nombre, apellido = None, edad = None, pais = None, ciudad = None):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.pais = pais
        self.ciudad = ciudad
        self.idiomas = []
    def saluda(self):
        print(f"Hola, soy {self.nombre}. Encantado de saludarte.")
    def datos(self):
        return {
            'nombre': self.nombre,
            'apellido': self.apellido,
            'edad': self.edad,
            'pais': self.pais,
            'ciudad': self.ciudad,
            'idiomas': self.idiomas
            }
    def añadir_idioma(self, idioma):
        self.idiomas.append(idioma)

persona1 = Persona("Pedro", apellido="Hernando", edad=54)
persona1.añadir_idioma('Inglés')
persona1.añadir_idioma('Español')
print(persona1.datos())


# Herencia

class Estudiante(Persona):
    pass

persona1 = Estudiante("Pedro", apellido="Hernando", edad=54)
persona1.añadir_idioma('Inglés')
persona1.añadir_idioma('Español')
print(persona1.datos())

## Modificando/Sobreescribiendo el constructor y otros métodos

class Estudiante(Persona):
    """Documentar"""
    # TODO: Documentar
    def __init__(self, nombre, apellido=None, edad=None, pais=None, ciudad=None):
        super().__init__(nombre, apellido, edad, pais, ciudad) # Si llamamos al constructor de la clase base, luego podemos añadir funcionalidad
        self.profesion = 'Estudiante'
    def saluda(self):
        # super().saluda() # Si no llamamos al método base, estamos anulando/sobreescribiendo su funcionalidad
        print(f"Hola, soy {self.nombre}. Encantado de saludarte. Soy estudiante.")
    def datos(self):
        datos = super().datos()
        datos['profesion'] = 'Estudiante'
        return datos


persona1 = Estudiante("Pedro", apellido="Hernando", edad=54)
persona1.añadir_idioma('Inglés')
persona1.añadir_idioma('Español')
persona1.saluda()
print(persona1.datos())
