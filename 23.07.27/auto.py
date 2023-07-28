import sqlite3

def naujas_automobilis():
    try:
        conn = sqlite3.connect('automobiliai.db')
        cursor = conn.cursor()

        marke = input("Įveskite automobilio markę: ")
        modelis = input("Įveskite automobilio modelį: ")
        spalva = input("Įveskite automobilio spalvą: ")
        pagaminimo_metai = int(input("Įveskite automobilio pagaminimo metus: "))
        kaina = float(input("Įveskite automobilio kainą: "))

        cursor.execute('''INSERT INTO Automobiliai (Marke, Modelis, Spalva, Pagaminimo_Metai, Kaina)
                          VALUES (?, ?, ?, ?, ?)''', (marke, modelis, spalva, pagaminimo_metai, kaina))
        conn.commit()

        print("Automobilis sėkmingai įrašytas į duomenų bazę.")
    except Exception as e:
        print("Klaida: ", e)
    finally:
        conn.close()

def ieskoti_automobiliu():
    try:
        conn = sqlite3.connect('automobiliai.db')
        cursor = conn.cursor()

        marke = input("Įveskite automobilio markę (palikite tuščią, jei nenorite ieškoti pagal markę): ")
        modelis = input("Įveskite automobilio modelį (palikite tuščią, jei nenorite ieškoti pagal modelį): ")
        spalva = input("Įveskite automobilio spalvą (palikite tuščią, jei nenorite ieškoti pagal spalvą): ")
        metai_min = int(input("Įveskite automobilio pagaminimo min metus (palikite tuščią, jei nenorite apriboti): ") or 0)
        metai_max = int(input("Įveskite automobilio pagaminimo max metus (palikite tuščią, jei nenorite apriboti): ") or 9999)
        kaina_min = float(input("Įveskite automobilio min kainą (palikite tuščią, jei nenorite apriboti): ") or 0.0)
        kaina_max = float(input("Įveskite automobilio max kainą (palikite tuščią, jei nenorite apriboti): ") or float('inf'))

        sql_query = '''SELECT * FROM Automobiliai WHERE Marke LIKE ? AND Modelis LIKE ? AND Spalva LIKE ? 
                       AND Pagaminimo_Metai BETWEEN ? AND ? AND Kaina BETWEEN ? AND ?'''

        cursor.execute(sql_query, (f'%{marke}%', f'%{modelis}%', f'%{spalva}%', metai_min, metai_max, kaina_min, kaina_max))
        results = cursor.fetchall()

        if not results:
            print("Nėra atitinkančių įrašų.")
        else:
            for row in results:
                print(row)

    except Exception as e:
        print("Klaida: ", e)
    finally:
        conn.close()

if __name__ == "__main__":
    while True:
        print("\n1. Įvesti naują automobilį")
        print("2. Ieškoti įrašų pagal visus stulpelius")
        print("3. Baigti programą")
        choice = input("Pasirinkite veiksmą (1/2/3): ")

        if choice == '1':
            naujas_automobilis()
        elif choice == '2':
            ieskoti_automobiliu()
        elif choice == '3':
            break
        else:
            print("Netinkamas pasirinkimas, bandykite dar kartą.")
