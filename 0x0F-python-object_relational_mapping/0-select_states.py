#!/usr/bin/python3
# AUTH: codenvibes
"""
This module lists all states from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states;")
    states = cursor.fetchall()
    for state in states:
        print(state)
    """
    The section of code is responsible for closing the cursor and the database connection. While the Python interpreter will automatically close the database connection when the program exits, it's generally a good practice to explicitly close it yourself, especially in larger or more complex programs.
    Closing the cursor and database connection is important because it releases the resources associated with them and can help prevent potential issues, such as resource leaks. It ensures that the database connection is properly terminated, and any associated system resources are released.
    In short, while the code will work without these lines, it's a good practice to include them to properly close the resources and follow best practices for managing database connections in Python.
    """
    cursor.close()
    db.close()
