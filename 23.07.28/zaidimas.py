import requests
from bs4 import BeautifulSoup
import time  # Import time module directly
import pickle
import sqlite3
import os

#senos DB ištrynimas
# if os.path.exists('quotes.db'):
#     # os.remove('quotes.db')
#
# #Konstantos
# URL = 'http://quotes.toscrape.com'
# conn = sqlite3.connect('quotes.db')
# c = conn.cursor()
#
# #Lentelės sukūrimas
# def make_database():
#     query = '''
#     CREATE TABLE IF NOT EXISTS quotes(
#         quote TEXT,
#         author TEXT,
#         hint1 TEXT,
#         hint2 TEXT
#     )
#     '''
#     with conn:
#         c.execute(query)
#
# def make_initials(name):
#     '''
#     funkcija, kuri iš paduoto teksto suformuoja inicialus
#     '''
#     splitted = name.split()
#     hint = ''
#     for i in splitted:
#         if '.' not in i:
#             hint += f'{i[0]}.'
#         else:
#             hint += i
#     return hint
#
# def get_hint2(endpoint):
#     '''
#     funkcija, kuri paduotą endpointą prideda prie URL ir ištraukia antrą užuominą
#     '''
#     r = requests.get(URL + endpoint)
#     soup = BeautifulSoup(r.text, "html.parser")
#     text = soup.select('p')[1].get_text()
#     return text
#
# def get_page(page):
#     r = requests.get(URL + '/page/' + str(page)).text
#     soup = BeautifulSoup(r, 'html.parser')
#     quotes = soup.select('.quote')
#     res = []
#     for i in quotes:
#         quote = i.find(class_='text').get_text()
#         author = i.find(class_='author').get_text()
#         hint1 = make_initials(author)
#         link = i.find('a', attrs={'class': None}).get('href')
#         hint2 = get_hint2(link)
#         sleep(0.2)
#         res.append((quote, author, hint1, hint2))
#     return res
#
# big_list = []
# for i in range(10):
#     big_list += get_page(str(i+1))
#
# make_database()
# with conn:
#     c.executemany('INSERT INTO quotes VALUES (?,?,?,?)', big_list)
# ... (Other parts of the code remain unchanged)

def play_game():
    conn = sqlite3.connect('quotes.db')
    cursor = conn.cursor()

    while True:
        cursor.execute('SELECT * FROM quotes ORDER BY RANDOM() LIMIT 1')
        quote = cursor.fetchone()

        text, author, hint = quote[0], quote[1], quote[2]

        print("Quote:")
        print(text)

        attempts = 3
        while attempts > 0:
            guess = input("Guess the author: ")

            if author and guess.lower() == author.lower():
                print("Correct! You guessed the author.")
                break
            else:
                attempts -= 1
                if attempts == 2:
                    if author:
                        print("First hint: Author's initials -", author[0])
                    else:
                        print("First hint: Author's initials are not available.")
                elif attempts == 1:
                    print(f"Second hint: The author was born {hint}")

        if attempts == 0:
            print(f"You didn't guess correctly. The correct answer is: {author}")

        continue_game = input("Do you want to continue? (yes/no): ")
        if continue_game.lower() != 'yes':
            break

        time.sleep(0.5)

    conn.close()

if __name__ == '__main__':
    play_game()
