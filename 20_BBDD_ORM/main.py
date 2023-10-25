import db
from models import Persona

def run():
    """Documentar"""
    # TODO: Documentar la función
    nuevo_cliente = Persona(nombre='Victor',apellido='Fernandez',edad=33)
    print(nuevo_cliente.pk)
    db.session.add(nuevo_cliente)
    print(nuevo_cliente.pk)
    db.session.commit()
    print(nuevo_cliente.pk)


if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)
    run()