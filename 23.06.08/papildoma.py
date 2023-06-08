import requests
from bs4 import BeautifulSoup
import random

def get_quote():
    response = requests.get('http://quotes.toscrape.com/')
    soup = BeautifulSoup(response.text, 'html.parser')

    quotes = soup.find_all('div', class_='quote')

    quote = random.choice(quotes)

    text = quote.find('span', class_='text').text
    author = quote.find('small', class_='author').text
    birth_date = quote.find('span', class_='author-born-date')
    birth_place = quote.find('span', class_='author-born-location')

    if birth_date is not None:
        birth_date = birth_date.text
    else:
        birth_date = "Gimimo datos informacija nerasta"

    if birth_place is not None:
        birth_place = birth_place.text
    else:
        birth_place = "Gimimo vietos informacija nerasta"

    return text, author, birth_date, birth_place

def play_game():
    attempts = 0
    while attempts < 3:
        text, author, birth_date, birth_place = get_quote()

        print("Citatą: ", text)
        guess = input("Kas yra citatos autorius? ")

        if guess.lower() == author.lower():
            print("Teisingai! Jūs atspėjote.")
            return

        attempts += 1
        if attempts == 1:
            print(f"Neteisingai. Pasufleruoju autoriaus inicialus: {author[0]}.")
        elif attempts == 2:
            print(f"Neteisingai. Pasufleruoju autoriaus gimimo datą ir vietą: {birth_date}, {birth_place}.")
        else:
            print(f"Neteisingai. Teisingas atsakymas yra: {author}.")

    print("Jūs nepateikėte teisingo atsakymo.")
    print(f"Teisingas atsakymas yra: {author}.")

# Pradedame žaidimą
play_game()

# Klausiame žaidėjo, ar nori tęsti žaidimą
while True:
    choice = input("Ar norite žaisti dar kartą? (taip / ne) ")
    if choice.lower() == "taip":
        play_game()
    elif choice.lower() == "ne":
        print("Ačiū, kad žaidėte!")
        break
    else:
        print("Neteisingas pasirinkimas. Bandykite dar kartą.")
