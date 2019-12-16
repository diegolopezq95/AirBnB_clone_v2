#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="delete", backref="state")

    @property
    def cities(self):
        """returns the list of City instances
        """
        my_list = []
        for key_obj, value in models.storage.all(City).items():
            if value["state_id"] == self.id:
                my_list.append(value)
        return my_list
