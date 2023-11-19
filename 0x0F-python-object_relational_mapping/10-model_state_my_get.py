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

    # Get the state name to search
    state_name = sys.argv[4]

    # Query for State object with the given name
    result_state = session.query(State).filter(State.name == state_name).first()

    # Display the result
    if result_state:
        print(result_state.id)
    else:
        print("Not found")

