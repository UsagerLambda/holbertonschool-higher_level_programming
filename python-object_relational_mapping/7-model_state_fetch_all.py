#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa"""

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

    # Crée une requete sur la table "State" qui trie tous les objets par id
    # (SELECT * FROM states ORDER BY id;)
    states = session.query(State).order_by(State.id).all()

    # parcours et imprime l'id et le nom de chaque State
    for state in states:
        print(f"{state.id}: {state.name}")

    # Fermer l'instance
    session.close()
