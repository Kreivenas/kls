class Person:
    def __init__(self, vardas, pavarde):
        self._vardas = vardas
        self._pavarde = pavarde

    @property
    def name(self):
        return self._vardas

    @name.setter
    def name(self, newnaujas_vardas):
        self._vardas = newnaujas_vardas

    @property
    def P_vardas(self):
        return f"{self._vardas} {self._pavarde}"

    def email(self):
        return f"{self._vardas.lower()}.{self._pavarde.lower()}@gmail.com"
