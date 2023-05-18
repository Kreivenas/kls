import random

def play_hangman():
    words = ["obuolys", "varna", "lopeta", "prisikiskekopustaliaudamas", "beglys"] # Sąrašas su žodžiais
    word = random.choice(words) # Atsitiktinis žodis
    guessed_letters = [] # Atspėtos raidės
    attempts = 5 # Spėjimų skaičius

    while True:
        hidden_word = ""
        for letter in word:
            if letter in guessed_letters:
                hidden_word += letter + " "
            else:
                hidden_word += "_ "

        print("Žodis:", hidden_word)
        print("Liko spėjimų:", attempts)

        guess = input("Įveskite raidę: ").lower()

        if guess in guessed_letters:
            print("Šią raidę jau spėjote!")

        elif guess in word:
            guessed_letters.append(guess)
            if set(word) == set(guessed_letters):
                print("Atspėjote žodį:", word)
                break

        else:
            print("Neteisingas atsakymas!")
            attempts -= 1
            if attempts == 0:
                print("Pralaimėjote! Teisingas žodis buvo:", word)
                break

    print("Žaidimas baigtas.")

play_hangman()
