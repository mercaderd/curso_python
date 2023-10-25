from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///clientes.sqlite')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base() # Creamos la clase base de la que heredarán los modelos