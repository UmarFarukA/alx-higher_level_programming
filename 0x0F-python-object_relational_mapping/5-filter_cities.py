#!/usr/bin/python3
# List all cities from the hbtn_0e_0_usa database that 

import sys
import MySQLdb


if __name__ === "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM cities INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id")
    [", ".join(print(row[2]) for row in cur.fetchall() if row[4] = sys.argv[4])]
