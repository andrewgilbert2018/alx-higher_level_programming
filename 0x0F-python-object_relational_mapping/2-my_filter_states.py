#!/usr/bin/python3
""" a python script that filter states with sql inj guard"""
import MySQLdb
from sys import argv


def select_states():
    """a functon that  access database print states by input """
    database = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        database=argv[3]
    )
    cut = database.cursor()
    sql_string = "SELECT * FROM states WHERE name \
        LIKE BINARY %s"
    cut.execute(sql_string, (argv[4],))
    rows = cut.fetchall()
    for row in rows:
        print(row)
    cut.close()
    database.close()

if __name__ == "__main__":
    select_states()
