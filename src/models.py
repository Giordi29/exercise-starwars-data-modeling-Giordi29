import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    surname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    fave_vehicles = relationship('Fave_Vehicles', back_populates='user')
    fave_chars = relationship('Fave_chars', back_populates='user')
    fave_plts = relationship('Fave_plts', back_populates='user') 

class Vehicles(Base):
    __tablename__ = 'Vehicles'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    model = Column(String(250), nullable=False)
    vehicle_name = Column(String(250), nullable=False)
    fave_vehicles = relationship('Fave_Vehicles', back_populates='vehicle')



class Fave_Vehicles(Base):
    __tablename__ = 'Fave_Vehicles'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("User.id"), nullable=False)
    vehicle_name = Column(Integer, ForeignKey("Vehicles.id"), nullable=False)
    user = relationship('User', back_populates='fave_vehicles')
    vehicle = relationship('Vehicles', back_populates='fave_vehicles')

class Characters(Base):
    __tablename__ = 'Characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    character_name = Column(String(250), nullable=False)
    fave_chars = relationship('Fave_chars', back_populates='character')
    planets = relationship('Planets', back_populates='character')

class Fave_chars(Base):
    __tablename__ = 'Fave_chars'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("User.id"), nullable=False)
    character_id = Column(Integer, ForeignKey("Characters.id"), nullable=False)
    user = relationship('User', back_populates='fave_chars')
    character = relationship('Characters', back_populates='fave_chars')

class Planets(Base):
    __tablename__ = 'Planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey("Characters.id"), nullable=False)
    character = relationship('Characters', back_populates='planets')
    fave_plts = relationship('Fave_plts', back_populates='planet')

class Fave_plts(Base):
    __tablename__ = 'Fave_plts'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("User.id"), nullable=False)
    planet_id = Column(Integer, ForeignKey("Planets.id"), nullable=False)
    user = relationship('User', back_populates='fave_plts')
    planet = relationship('Planets', back_populates='fave_plts')

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e



