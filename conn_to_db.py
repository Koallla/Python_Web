from sqlalchemy import Date, Column, ForeignKey, Integer, Sequence, String 
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///sqlalchemy_example.db')
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()

Base = declarative_base()


class UserRecord(Base):
    __tablename__ = 'records'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    adress = Column(String(200), nullable=False)
    note = Column(String(500))
    tag = Column(String(200))
    email = Column(String(200), nullable=False)
    phone = Column(String(300), nullable=False)
    birthday = Column(Date(), nullable=False)


# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)



Base.metadata.create_all(engine)
Base.metadata.bind = engine



# new_person = Person(name="Bill")
# session.add(new_person)
# session.commit()


# new_address = Address(post_code='00000', person=new_person)
# session.add(new_address)
# session.commit()


# for person in session.query(Person).all():
#     print(person.name)  # Bill


# for address in session.query(Address).all():
#     print(address.post_code)  


def upgrade():
    op.create_table(
        'records',
        sa.Column('id', sa.Integer, sa.Sequence('user_id_seq'), primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('surname', sa.String(50), nullable=False),
        sa.Column('adress', sa.String(200), nullable=False),
        sa.Column('note', sa.String(500)),
        sa.Column('tag', sa.String(200)),
        sa.Column('email', sa.String(200), nullable=False),
        sa.Column('phone', sa.String(300), nullable=False),
        sa.Column('birthday', sa.Date(), nullable=False),
    )

    op.bulk_insert(records,
    [{'name': 'Mihail', 'surname': 'Zmiiov', 'adress': 'Kyiv, Dryzby Narodov 26/1', 'email': 'z@i.ua', 'phone': '380953128882', 'birthday': '1983 07 22'}])