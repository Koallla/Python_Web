from sqlalchemy import Column, Integer, String

from database import Base



class Comand(Base):

    __tablename__ = "comand"

    id = Column(Integer, primary_key=True, index=True)
    rating = Column(Integer)
    logo = Column(String(500))
    name = Column(String(250), unique=True, index=True)
    games = Column(Integer)
    wins = Column(Integer)
    draws = Column(Integer)
    losses = Column(Integer)
    goals_in = Column(Integer)
    goals_out = Column(Integer)
    difference = Column(Integer)
    scores = Column(Integer)