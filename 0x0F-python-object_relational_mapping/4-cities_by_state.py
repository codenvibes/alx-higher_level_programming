#!/usr/bin/python3
# AUTH: codenvibes
"""
This module lists all cities from the database hbtn_0e_4_usa.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities JOIN states\
        ON cities.state_id = states.id;"
    cursor.execute(query)
    states = cursor.fetchall()
    for match in states:
        print(match)
    cursor.close()
    db.close()
