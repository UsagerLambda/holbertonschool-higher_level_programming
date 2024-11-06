#!/usr/bin/python3
"""prints the first State object from the database hbtn_0e_6_usa"""

from sqlalchemy import create_engine
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

    # (SELECT * FROM states ORDER BY id ASC LIMIT 1;)
    states = session.query(State).first()

    if states:
        print(f"{states.id}: {states.name}")
    else:
        print("Nothing")

    # Fermer l'instance
    session.close()
