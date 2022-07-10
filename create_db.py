import sqlite3

conn = sqlite3.connect('phones.db')
cur = conn.cursor()

cur.execute('''
CREATE TABLE phones
(ContactName varchar(100), Phones varchar(20) UNIQUE)
''')

conn.commit()
conn.close()
