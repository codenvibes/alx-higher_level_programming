#!/usr/bin/python3
# AUTH: codenvibes
"""
This module lists all State objects from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(username, password, database_name),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.close()
    first_state = session.query(State).order_by(State.id).first()
    if first_state is not None:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")
    session.close()
