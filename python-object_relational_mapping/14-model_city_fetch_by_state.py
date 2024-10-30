#!/usr/bin/python3
"""script 14-model_city_fetch_by_state.py that prints all City objects"""

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State
from model_city import City  # import City


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
        session.query(State, City)  # selectionne State et City
        .join(City)  # join City à State
        .order_by(State.id.asc())
        .all()
        )

    for state, city in states:
        print(f'{state.name}: ({city.id}) {city.name}')

    # Fermer l'instance
    session.close()