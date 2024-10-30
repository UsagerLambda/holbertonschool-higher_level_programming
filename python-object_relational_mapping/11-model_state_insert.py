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

    # assigne à new_state une instance de State
    # prenant un argument name ayant pour valeur Louisiana
    new_state = State(name="Louisiana")
    session.add(new_state)  # ajoute l'objet à session (l19)
    session.commit()  # commit les modif de session dans la database

    print(new_state.id)


    # Fermer l'instance
    session.close()
