#!/usr/bin/python3
# Using sqlalchmemy to list all states


import sys
from sqlalachemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id)
    for state in states:
        print("{} {}".format(state.id, state.name))
