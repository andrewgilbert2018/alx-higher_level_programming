#!/usr/bin/python3
""" a python script that fetch all states """
from model_state import Base, State
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def add_state():
    """ funtion that access database and print states """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = State(name="Louisiana")
    session.add(state)
    session.commit()
    print(state.id)
    session.close()
if __name__ == "__main__":
    add_state()
