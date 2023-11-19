#!/usr/bin/python3
"""
Contains State class and Base, an instance of declarative_base()
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class State(Base):
    """
    Class with id and name attributes of each state
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    import sys
    from urllib.parse import quote_plus

    # Constructing the connection string components
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Encode the password to handle special characters
    encoded_password = quote_plus(password)

    # Construct the connection string with encoded password
    connection_string = f"mysql+mysqldb://{username}:{encoded_password}@localhost/{database}"

    # Create the engine
    engine = create_engine(connection_string, pool_pre_ping=True)

    # Create all tables in the engine
    Base.metadata.create_all(engine)
