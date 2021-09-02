from soup import add_commands_to_db
from sqlalchemy.orm import Session


from models import Comand
from schemas import ComandCreate



def crud_download_comands(db: Session):
    return add_commands_to_db(db)



def crud_get_comand(db: Session, comand_id: int):
    return db.query(Comand).filter(Comand.id == comand_id).first()


def crud_get_comands(db: Session, skip: int = 0, limit: int = 20):
    return db.query(Comand).offset(skip).limit(limit).all()


def crud_create_comand(db: Session, comand: ComandCreate):

    db_comand = Comand(
    rating = comand.rating,
    logo = comand.logo,
    name = comand.name,
    games = comand.games,
    wins = comand.wins,
    draws = comand.draws,
    losses = comand.losses,
    goals_in = comand.goals_in,
    goals_out = comand.goals_out,
    scores = comand.scores
    )


    db.add(db_comand)
    db.commit()
    db.refresh(db_comand)
    return db_comand

