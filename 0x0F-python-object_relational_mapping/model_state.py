#!/usr/bin/python3
"""Represent the state class"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """A class definition of State
       which extends the Base class that represents
       MYSQL table.
       __tablename__: name the tables as state
       id (Integer): represent that table id column
       name (string): represents the a column, name
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
