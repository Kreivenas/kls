import sqlite3

conn = sqlite3.connect('zmones.db')
c = conn.cursor()

query = '''
CREATE TABLE IF NOT EXISTS draugai (
    f_name VARCHAR(50),
    l_name VARCHAR(50),
    email VARCHAR(100)
);
'''

c.execute(query)
conn.commit()