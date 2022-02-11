import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    favorites= relationship("Favorites", back_populates="parent")
    
class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(250)) 
    height = Column(String(250))
    mass = Column(String(250))
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    eye_color = Column(String(250))
    birth_year = Column(String(250))
    gender = Column(String(250))
    favorites_id= Column(Integer, ForeignKey("favorites.id"))
    favorites= relationship("Favorites", back_populates="children")

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250)) 
    diameter = Column(String(250))
    population = Column(String(250))
    climate = Column(String(250))
    terrain = Column(String(250))
    surface_water = Column(String(250))
    gravity = Column(String(250))
    rotation_period = Column(String(250))
    favorites_id= Column(Integer, ForeignKey("favorites.id"))
    favorites= relationship("Favorites", back_populates="children")
    
class Vehicle(Base):
    __tablename__ ="vehicle"
    id = Column(Integer, primary_key=True)
    model = Column(String(250)) 
    vehicle_class = Column(String(250))
    manufacturer = Column(String(250))
    cost_in_credits = Column(Integer)
    length = Column(Integer)
    crew = Column(Integer)
    passengers = Column(Integer)
    max_atmosphering_speed = Column(Integer)
    favorites_id= Column(Integer, ForeignKey("favorites.id"))
    favorites= relationship("Favorites", back_populates="children") 
    
    
class Favorites(Base):
    __tablename__ = 'favorites'
    id= Column(Integer, primary_key=True)
    user_id= Column(Integer, ForeignKey("user.id"))
    user= relationship("User", back_populates="children")
    people= relationship("People", back_populates="children")
    planet= relationship("Planet", back_populates="children")
    vehicle= relationship("Vehicle",back_populates="children")





## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')