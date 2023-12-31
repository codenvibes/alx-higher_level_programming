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
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'\
                   ORDER BY states.id ASC".format(sys.argv[4]))
    states = cursor.fetchall()
    for match in states:
        print(match)
    cursor.close()
    conn.close()
