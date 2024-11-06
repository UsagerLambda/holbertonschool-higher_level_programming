#!/usr/bin/python3
"""Define Cities class"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base  # importe Base de model State
from sqlalchemy.orm import relationship


class City(Base):
    """SQL City table"""

    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    # Relation avec la classe State
    state = relationship("State", back_populates="cities")
