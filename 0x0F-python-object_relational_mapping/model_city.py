#!/usr/bin/python3
"""Represent the city class"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Represent the city class
    __tablename__: Defines the table name
    id: Table Id
    name: represents name of city
    state_id: A foreign key
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    state = relationship("State", back_populates="cities")
