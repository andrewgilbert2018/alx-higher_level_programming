#!/usr/bin/python3
""" a python script that defines city, state"""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """ defines City class """
    __tablename__ = 'cities'
    id = Column(
                Integer,
                autoincrement=True,
                unique=True,
                nullable=False,
                primary_key=True
                )
    name = Column(
                  String(128),
                  nullable=False
                  )
    state_id = Column(
                      Integer,
                      ForeignKey("states.id"),
                      nullable=False,
                      )
