#!/usr/bin/python3
"""Scripts that print the state which contains letter a"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(State).join(City).order_by(City.id).all()
    for c, s in cities:
        print("{}: ({}) {}".format(s.name, c.id, c.name))
