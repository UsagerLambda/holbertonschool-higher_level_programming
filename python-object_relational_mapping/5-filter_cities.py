#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    conn = MySQLdb.connect(
        host='localhost',
        user=mysql_username,
        password=mysql_password,
        db=database_name,
        port=3306
        )

    cursor = conn.cursor()
    requete = (
        "SELECT cities.name FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC")
    cursor.execute(requete, (state_name,))
    results = cursor.fetchall()

    print(", ".join(city[0] for city in results))

    cursor.close()
    conn.close()
