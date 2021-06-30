from helpers import show_table

from sqlalchemy import Date, Column, ForeignKey, Integer, Sequence, String 
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


engine = create_engine('sqlite:///records.db', echo=True)
session = Session(bind=engine)
Base = declarative_base()


class UserRecord(Base):
    __tablename__ = 'records'

    def __init__(self, name, surname, adress, note, tag, email, phone, birthday):
        self.name = name
        self.surname = surname
        self.adress = adress
        self.note = note
        self.tag = tag
        self.email = email
        self.phone = phone
        self.birthday = birthday

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    adress = Column(String(50), nullable=False)
    note = Column(String(150), nullable=False)
    tag = Column(String(80), nullable=False)
    email = Column(String(80), nullable=False)
    phone = Column(String(11), nullable=False)
    birthday = Column(String(), nullable=False)



Base.metadata.create_all(engine)
Base.metadata.bind = engine


def add_new_record(record):
    session.add(record)
    session.commit()



def create_new_record(rec):
    new_record = UserRecord(rec.name, rec.surname, rec.adress, rec.note, rec.tag, rec.email, rec.phone, rec.birthday)
    add_new_record(new_record)
    



class FindDataInDb():
    records_list = []

    def show_records_for_name(self, name):
        full_rec = {}

        for rec in session.query(UserRecord).filter(UserRecord.name == name):
            full_rec['id'] = rec.id
            full_rec['name'] = rec.name
            full_rec['surname'] = rec.surname
            full_rec['adress'] = rec.adress
            full_rec['note'] = rec.note,
            full_rec['tag'] = rec.tag,
            full_rec['email'] = rec.email,
            full_rec['phone'] = rec.phone,
            full_rec['birthday'] = rec.birthday
            self.records_list.append(full_rec)
            full_rec = {}
        
        print(show_table(self.records_list))


