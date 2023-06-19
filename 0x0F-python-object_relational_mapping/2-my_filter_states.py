#!/usr/bin/python3
""" a python script that filter states """
import MySQLdb
from sys import argv


def select_states():
    """ a function that  access database and  print states by input """
    database = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        database=argv[3]
    )
    current = database.cursor()
    sql_string = "SELECT * FROM states WHERE name \
        LIKE BINARY '{}'".format(argv[4])
    current.execute(sql_string)
    rows = current.fetchall()
    for row in rows:
        print(row)
    current.close()
    database.close()

if __name__ == "__main__":
    select_states()
