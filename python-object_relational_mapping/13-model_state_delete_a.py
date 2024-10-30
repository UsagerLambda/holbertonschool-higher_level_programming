#!/usr/bin/python3
"""deletes all State objects with a name containing the letter a"""

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State


# le if exécute le code uniquement si le script est lancé directement
if __name__ == "__main__":
    # établie une connexion à une base de données avec les arguments fournis
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Crée une class Session liée à engine
    Session = sessionmaker(bind=engine)
    # Crée une instance de la class Session
    session = Session()

    states = (
        session.query(State)
        .filter(State.name.like('%a%'))
        .all()
        )

    for state in states:
        session.delete(state)
    session.commit()

    # Fermer l'instance
    session.close()
