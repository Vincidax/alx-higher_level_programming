#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    stmt = """
        SELECT cities.name
        FROM cities
        INNER JOIN states ON cities.state_id = states.id
        WHERE states.name LIKE %s
        """
    c_s = sys.argv[4]
    cur.execute(stmt, (c_s, ))
    rows = cur.fetchall()
    city_names = [row[0] for row in rows]

    print(', '.join(city_names))

    # for row in rows:
    #    print(row, end=', ')
    cur.close()
    db.close()
