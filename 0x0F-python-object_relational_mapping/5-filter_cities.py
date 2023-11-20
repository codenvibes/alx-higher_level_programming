#!/usr/bin/python3
# AUTH: codenvibes
"""
This module takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    query = "SELECT cities.name, states.name FROM cities JOIN states ON\
        cities.state_id = states.id WHERE states.name LIKE BINARY %s;"
    state_name = sys.argv[4]
    cursor.execute(query, (state_name,))
    cities_in_state = cursor.fetchall()
    for city in cities_in_state:
        print(city)
    cursor.close()
    db.close()
