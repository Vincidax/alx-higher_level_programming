#!/usr/bin/env python

import MySQLdb
import sys


def list_states(username, password, db_name):
    # Connect to MySQL server
    db = MySQLdb.connect(
        host='localhost',
        user=username,
        passwd=password,
        db=db_name,
        port=3306
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query to retrieve states
    query = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(query)

    # Fetch all results
    results = cursor.fetchall()

    # Display results
    for row in results:
        print(row)

    # Close cursor and connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    # Take arguments from command line
    if len(sys.argv) != 4:
        print("Usage: {} username password database_name".format(sys.argv[0]))
        sys.exit(1)

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Call the function with provided arguments
    list_states(username, password, db_name)

