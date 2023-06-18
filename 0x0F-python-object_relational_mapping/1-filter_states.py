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
    cut = database.cursor()
    cut.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")
    rows = cut.fetchall()
    for row in rows:
        print(row)
    cut.close()
    database.close()


if __name__ == "__main__":
    select_states()
