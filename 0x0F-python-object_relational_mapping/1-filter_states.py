#!/usr/bin/python3
# AUTH: codenvibes
"""
This module lists all states with a name starting with N (upper N) from the
database hbtn_0e_0_usa:
"""
import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states")
    states = cursor.fetchall()
    # stwn - states starting with N
    for stwn in states:
        if stwn[1][0] == "N":
            print(stwn)
    cursor.close()
    conn.close()
