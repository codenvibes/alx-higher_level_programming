#!/usr/bin/python3
# AUTH: codenvibes
"""
This module lists all State objects that contain the letter a from the
database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(username, password, database_name),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for State objects containing the letter 'a'
    result = session.query(State).filter(State.name.like("%a%"))\
        .order_by(State.id).all()
    for state in result:
        print("{}: {}".format(state.id, state.name))
    session.close()
