#/usr/bin/python3

# Useful stuff:
# https://docs.python.org/3.6/library/sqlite3.html

print("### begin read.py ###")

import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

for row in c.execute('SELECT * FROM test'):
    print (row)

conn.commit()
conn.close()

print("### end read.py ###")
