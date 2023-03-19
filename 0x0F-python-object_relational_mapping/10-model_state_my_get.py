#!/usr/bin/python3
"""Scripts that print the state id base on what user entered"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State)
    found = False
    for state in states:
        if state.name == sys.argv[4]:
            print("{}".format(state.id))
            found = True
            break
    if not found:
        print("Not found")
