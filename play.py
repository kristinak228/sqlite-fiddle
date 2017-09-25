#/usr/bin/python3

# Useful stuff:
# https://docs.python.org/3.6/library/sqlite3.html

print("######")

import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('''CREATE TABLE test (thing text, that text)''')
c.execute('''INSERT INTO test VALUES ('thing', 'thing2')''')

for row in c.execute('SELECT * FROM test'):
    print (row)

conn.commit()
conn.close()

print("######")
