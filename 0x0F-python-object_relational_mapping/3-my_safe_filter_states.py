#!/usr/bin/python3
# AUTH: codenvibes
"""
This module takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = conn.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY %s\
                   ORDER BY states.id ASC"
    state_name = sys.argv[4]
    cursor.execute(query, (state_name,))
    states = cursor.fetchall()
    for match in states:
        print(match)
    cursor.close()
    conn.close()
