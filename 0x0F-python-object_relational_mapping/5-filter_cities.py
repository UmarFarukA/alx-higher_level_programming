#!/usr/bin/python3
"""List all cities of a states"""

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    query = "SELECT * FROM cities INNER JOIN states\
             ON cities.state_id = states.id ORDER BY cities.id"
    cur.execute(query)
    print(", ".join([row[2] for row in cur.fetchall()
          if row[4] == sys.argv[4]]))
    cur.close()
    db.close()
