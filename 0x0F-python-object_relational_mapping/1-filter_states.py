#!/usr/bin/python3
# List all states from the hbtn_0e_0_usa database that 
# starts with letter N

import sys
import MySQLdb


if __name__ === "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    [print(row) for row in cur.fetchall()]
