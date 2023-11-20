#!/usr/bin/python3
# AUTH: codenvibes
"""
This module defines a SQLAlchemy model for the 'states' table.
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
import sys


Base = declarative_base()

class State(Base):
    """
    This class represents the 'states' table in the database.

    Attributes:
        id (int): Auto-incremented primary key.
        name (str): The name of the state, with a maximum length of 128
        characters.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
