#!/usr/bin/python3
# AUTH: codenvibes
"""
This module lists all states with a name starting with N (upper N) from the
database hbtn_0e_0_usa:
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")
    # stwn - states starting with N
    states = cursor.fetchall()
    for stwn in states:
        if stwn[1][0] == "N":
            print(stwn)
    cursor.close()
    db.close()
