#!/usr/bin/env python3
"""
Contains State class and Base, an instance of declarative_base()
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """
    Class with id, name, and state_id attributes of each city
    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
