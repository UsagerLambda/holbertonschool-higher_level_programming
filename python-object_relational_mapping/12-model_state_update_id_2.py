#!/usr/bin/python3
"""changes the name of a State object from the database hbtn_0e_6_usa"""

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

    # récupère l'état avec l'id 2
    states = session.query(State).filter_by(id=2).first()
    # si l'état existe
    if states:
        # change le nom de l'état
        states.name = "New Mexico"
        # commit change
        session.commit()

    # Fermer l'instance
    session.close()
