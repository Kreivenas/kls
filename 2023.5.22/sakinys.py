class Sakinys:
    def __init__(self, tekstas):
        self.tekstas = tekstas

    def atbulai(self):
        return self.tekstas[::-1]

    def mazosiomis(self):
        return self.tekstas.lower()

    def didziosiomis(self):
        return self.tekstas.upper()

    def zodis(self, numeris):
        zodziai = self.tekstas.split()
        if numeris >= 1 and numeris <= len(zodziai):
            return zodziai[numeris - 1]
        else:
            return "Nurodytas žodis neegzistuoja."

    def skaicius_zodziuose(self, simboliai):
        zodziai = self.tekstas.split()
        kiekis = 0
        for zodis in zodziai:
            if simboliai.lower() in zodis.lower():
                kiekis += 1
        return kiekis

    def pakeisti_zodi(self, senas_zodis, naujas_zodis):
        return self.tekstas.replace(senas_zodis, naujas_zodis)

    def spausdinti_statistika(self):
        zodziai = len(self.tekstas.split())
        skaiciai = sum(char.isdigit() for char in self.tekstas)
        didziosios = sum(char.isupper() for char in self.tekstas)
        mazosios = sum(char.islower() for char in self.tekstas)

        print("Žodžių skaičius:", zodziai)
        print("Skaičių skaičius:", skaiciai)
        print("Didžiųjų raidžių skaičius:", didziosios)
        print("Mažųjų raidžių skaičius:", mazosios)

