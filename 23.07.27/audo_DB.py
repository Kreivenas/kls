import sqlite3

# Sukuriamas SQLite duomenų bazės failas
conn = sqlite3.connect('automobiliai.db')
cursor = conn.cursor()

# Sukuriamos lentelės "Automobiliai"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Automobiliai (
        ID INTEGER PRIMARY KEY,
        Marke TEXT,
        Modelis TEXT,
        Spalva TEXT,
        Pagaminimo_Metai INTEGER,
        Kaina REAL
    )
''')

# Uždarome ryšį su duomenų baze
conn.commit()
conn.close()
