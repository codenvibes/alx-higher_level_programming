#!/usr/bin/python3
"""Start link class to table in database 
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True) # https://github.com/codenvibes/alx-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/6-model_state.md
    Base.metadata.create_all(engine) # This line creates the tables defined in the SQLAlchemy model. The Base.metadata.create_all(engine) call instructs SQLAlchemy to create the database tables associated with the classes defined in the Base using the provided database engine
