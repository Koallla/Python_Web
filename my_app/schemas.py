from pydantic import BaseModel


class ComandBase(BaseModel):
    rating: int
    logo: str
    name: str
    games: int
    wins: int
    draws: int
    losses: int
    goals_in: int
    goals_out: int
    difference: int
    scores: int
    


class ComandCreate(ComandBase):
    pass


class Comand(ComandBase):
    id: int

    class Config:
        orm_mode = True
