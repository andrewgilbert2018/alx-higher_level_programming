#!/usr/bin/python3
"""a python script that help to select states from a server """
import MySQLdb
from sys import argv


def select_states():
    """function to access database and  print states """
    database = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        database=argv[3]
    )
    current = database.cursor()
    current.execute("SELECT * FROM states ORDER BY id")
    rows = current.fetchall()
    for row in rows:
        print(row)
    current.close()
    database.close()


if __name__ == "__main__":
    select_states()
