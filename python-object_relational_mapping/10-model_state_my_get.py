#!/usr/bin/python3
"""lists State that contain the letter a in database hbtn_0e_6_usa"""

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

    # (SELECT * FROM states WHERE name = argv[4] LIMIT 1;)
    states = (
        session.query(State)
        .filter(State.name == sys.argv[4])
        .first()
        )

    if states:
        print(states.id)
    else:
        print("Not found")

    # Fermer l'instance
    session.close()
