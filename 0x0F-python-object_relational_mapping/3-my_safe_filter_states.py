#!/usr/bin/python3
"""
Module that connects a python script to a database
"""

if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    # Connect database using command-line arguments
    my_db = MySQLdb.connect(
        host='localhost',
        user=argv[1],
        password=argv[2],
        db=argv[3],
        port=3306
        )
    # Creating cursor obj to interact with db
    my_cursor = my_db.cursor()

    # ExecuteSELECT query
    my_cursor.execute(
            "SELECT * FROM states WHERE name=%s ORDER BY id", (argv[4], ))

    # Fetch all the daya required by the query
    my_data = my_cursor.fetchall()

    # iterate through the fetched data and print each row
    for row in my_data:
        print(row)

    # close all cursors
    my_cursor.close()

    # close db
    my_db.close()
