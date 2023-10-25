import db
from models import Persona

def run():
    """Documentar"""
    # TODO: Documentar la función
    with open('./datos.csv', encoding='utf-8') as f:
        lineas = f.readlines()
        for linea in lineas[1:]:
            nombre,apellido,edad = linea.split(sep=',')
            nuevo_cliente = Persona(nombre=nombre, apellido=apellido,edad=int(edad))
            print(nuevo_cliente.pk)
            db.session.add(nuevo_cliente)
            print(nuevo_cliente.pk)
            db.session.commit()
            print(nuevo_cliente.pk)
            print(nuevo_cliente)


if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine) # Crea las tablas si no existen.
    run()