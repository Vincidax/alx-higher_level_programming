#!/usr/bin/python3
"""Lists all State objects that contain the letter a
    from the database hbtn_0e_6_usa
    """

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

    # Query for State objects containing the letter 'a'
    result_states = session.query(State).filter(
        State.name.like('%a%')
    ).order_by(State.id).all()

    for state in result_states:
        session.delete(state)
    session.commit()
