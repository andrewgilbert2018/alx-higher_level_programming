#!/usr/bin/python3
""" a python script that fetch state by input """
from model_state import Base, State
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def fetch_states():
    """ a function that access database and print state """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    state = session.query(State).filter(State.name == argv[4]).first()
    if state:
        print(state.id)
    else:
        print("Not found")
    session.close()


if __name__ == "__main__":
    fetch_states()
