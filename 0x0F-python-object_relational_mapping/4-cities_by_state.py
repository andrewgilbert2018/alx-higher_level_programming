#!/usr/bin/python3
""" a python script that select cities by state """
import MySQLdb
from sys import argv


def select_cities():
    """function to  access database and  print states by input """
    database = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        database=argv[3]
    )
    cu = database.cursor()
    sql_string = "SELECT cities.id, cities.name, states.name FROM cities \
        INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id"
    cu.execute(sql_string)
    rows = cu.fetchall()
    for row in rows:
        print(row)
    cu.close()
    database.close()


if __name__ == "__main__":
    select_cities()
