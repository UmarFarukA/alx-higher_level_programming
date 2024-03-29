#!/usr/bin/python3
"""List all cities from the hbtn_0e_0_usa database"""

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM\
             cities INNER JOIN states ON\
             cities.state_id = states.id ORDER BY cities.id"
    cur.execute(query)
    [print(row) for row in cur.fetchall()]
    cur.close()
    db.close()
