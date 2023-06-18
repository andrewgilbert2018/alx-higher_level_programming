#!/usr/bin/python3
"""python script to filter states """
import MySQLdb
from sys import argv


def select_states():
    """ access database and  print states that  start with N """
    database = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        database=argv[3]
    )
    current = database.cursor()
    current.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")
    rows = curent.fetchall()
    for row in rows:
        print(row)
    current.close()
    database.close()


if __name__ == "__main__":
    select_states()
