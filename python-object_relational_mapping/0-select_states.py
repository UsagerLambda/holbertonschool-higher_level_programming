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

    conn = MySQLdb.connect(
        host='localhost',
        user=mysql_username,
        password=mysql_password,
        db=database_name,
        port=3306
        )

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id")
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    conn.close()