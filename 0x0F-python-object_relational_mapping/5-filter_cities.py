#!/usr/bin/python3
""" a python script that select cities by state """
import MySQLdb
from sys import argv


def select_cities():
    """ function that  access database and print states by input """
    database = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        database=argv[3]
    )
    cu = database.cursor()
    sql_string = "SELECT cities.name FROM cities \
        INNER JOIN states ON cities.state_id = states.id \
        WHERE states.name LIKE BINARY %s ORDER BY cities.id"
    cu.execute(sql_string, (argv[4],))
    rows = cu.fetchall()
    row_count = 0
    row_end = len(rows)
    if rows:
        for row in rows:
            city = str(row).strip("(')")
            city = city.replace("',", "")
            row_count += 1
            if row_count == row_end:
                print(city)
            else:
                print(city, end=", ")
    else:
        print("")
    cu.close()
    database.close()


if __name__ == "__main__":
    select_cities()
