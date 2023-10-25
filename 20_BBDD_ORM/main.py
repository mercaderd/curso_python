import db
from models import Persona

def cargar_datos():
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

def consultar_datos():
    """Documentar"""
    num_clientes = db.session.query(Persona).count()
    print(f"El total de clientes es {num_clientes}")
    clientes = db.session.query(Persona).all() # Obtener todos las filas de una tabla
    for cliente in clientes:
        print(cliente)
    # Otras consultas
    print(db.session.query(Persona).filter_by(nombre='victor').first())
    print(db.session.query(Persona).filter(Persona.edad > 18).all())
    # Borrar una fila
    print(db.session.query(Persona).count())
    cliente = db.session.query(Persona).filter_by(nombre='victor').first()
    if cliente: 
        db.session.delete(cliente)
    db.session.commit()
    print(db.session.query(Persona).count())
    


if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine) # Crea las tablas si no existen.
    # cargar_datos()
    consultar_datos()