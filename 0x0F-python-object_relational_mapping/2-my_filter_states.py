#!/usr/bin/python3
"""List all states from the hbtn_0e_0_usa database
   search base on user input
"""

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    query = "SELECT * FROM states WHERE BINARY name = '{}'"
    .format(sys.argv[4])
    cur.execute(query)
    [print(row) for row in cur.fetchall()]
