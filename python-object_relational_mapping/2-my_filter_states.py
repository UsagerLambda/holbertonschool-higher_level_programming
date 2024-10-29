#!/usr/bin/python3
"""
Module pour afficher toutes les entrées de la table `states`
triées par `id` dans une base de données MySQL.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    conn = MySQLdb.connect(
        host='localhost',
        user=mysql_username,
        password=mysql_password,
        db=database_name,
        port=3306
        )

    cursor = conn.cursor()
    requete = (
        "SELECT * FROM states "
        "WHERE name = '{}' "
        "ORDER BY states.id ASC").format(state_name_searched)
    cursor.execute(requete)
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    conn.close()
