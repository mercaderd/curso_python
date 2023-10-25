import db      # El módulo en el que se ha creado el engine, la sesión y la clase Base

from sqlalchemy import Column, Integer, String, Float

class Persona(db.Base):
    # TODO: Documentar la clase
    __tablename__ = 'Persona'
    pk = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    edad = Column(Integer,nullable=True)
