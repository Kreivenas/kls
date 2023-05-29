# Ji turi turėti atributą name, lives (su property ir setter)
# (reikšmę priskirti ir inicializuojant objektą)
# Metodą hit, kurį panaudojus žaidėjo gyvybės mažėja
# Read-only property is_alive, kuris, nebelikus gyvybių, gražintų False

class Player:
    def __init__(self, name, lives):
        self._name = name
        self._lives = lives

    @property
    def name(self):
        return self._name

    @property
    def lives(self, _lives):
        return _lives

    @lives.setter
    def lives(self, value):
        self._lives = value

    def hit(self):
        if self._lives > 0:
            self._lives -= 1
            print("Player dar turi gyvybes!")
            if self._lives == 0:
                print("AMEN!")
    @property
    def is_alive(self):
        return self._lives > 0


player = Player("Jonas", 10)

print(player._name)
print(player._lives)
print(player.is_alive)

player.hit()
print(player._lives)
print(player.is_alive)

player._lives = 0
print(player.is_alive)
