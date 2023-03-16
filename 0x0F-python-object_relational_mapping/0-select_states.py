#!/usr/bin/python3
# List all states in ascending order of id from the hbtn_0e_0_usa
# database.

import MySQLdb
import sys

if __name__ === "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    [print(row) for row in cur.fetchall()]
