#!/usr/bin/python3
"""Prints the State object with the name passed as an argument
    from the database hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        )
    )

    # Bind the engine to the metadata of the Base class
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Retrieve the State object where id = 2
    state_to_update = session.query(State).filter_by(id=2).first()

    # Change the name of the state
    state_to_update.name = 'New Mexico'
    session.commit()  # Commit the transaction to the database
