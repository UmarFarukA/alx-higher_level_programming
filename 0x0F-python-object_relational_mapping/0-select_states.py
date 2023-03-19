#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == "__main__":
    """Listing all states from hbtn_0e_0_usa database"""
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    [print(state) for state in cur.fetchall()]
    cur.close()
    db.close()
