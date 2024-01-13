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

    # Create cursor obj to interact with db
    my_cursor = my_db.cursor()

    # Execute SEKECT query
    my_cursor.execute(
            """SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states
        ON states.id = cities.state_id
        ORDER BY cities.id"""
    )

    # fetch all data from the query
    my_data = my_cursor.fetchall()

    # Iterate through the data and print each row
    for row in my_data:
        print(row)

    # close cursor
    my_cursor.close()

    # close db
    my_db.close()
