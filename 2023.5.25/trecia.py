# Sukurti programą, kuri:
#
# Turėtų klasę Automobilis
# Automobilis turėtų savybes: metai, modelis, kuro_tipas
# Automobilis turėtų metodus: vaziuoti, stoveti, pildyti_degalu,
# kurie atitinkamai atspausdintų „Važiuoja“, „Priparkuota“, „Degalai įpilti“
# Sukūrus objektą, automatiškai atspausdintų automobilio metus, modelį ir kuro tipą
# Turėtų klasę Elektromobilis (jo tėvinis objektas – Automobilis)
# Elektromobilis pakeistų Automobilio metodą pildyti_degalu taip,
# kad jis atspausdintų „Baterija įkrauta“
# Elektromobilis turėtų metodą vaziuoti_autonomiskai, kuris spausdintų
# „Važiuoja autonomiškai“
# Sukurti norimą Automobilio objektą
# Sukurti norimą Elektromobilio objektą
# Su sukurtu Automobilio objektu paleisti funkcijas vaziuoti, stoveti, pildyti_degalu
# Su sukurtu Elektromobilio objektu paleisti funkcijas vaziuoti, stoveti,\
#     pildyti_degalu, vaziuoti_autonomiskai
class Automobilis:
    def __init__(self, metai, modelis, kuro_tipas):
        self.metai = metai
        self.modelis = modelis
        self.kuro_tipas = kuro_tipas

    def __str__(self):
        return f'{self.metai}, {self.modelis}, {self.kuro_tipas}'

    def vaziuoti(self):
        print("Vaziuoja")

    def stoveti(self):
        print("Priparkuota")

    def pildyti_degalu(self):
        print("Degalai įpilti")

mano_auto = Automobilis(2022, "Audi", "Dyzelinas")
mano_auto.vaziuoti()
mano_auto.stoveti()
mano_auto.pildyti_degalu()
print(mano_auto)

class Elektromobilis(Automobilis):

    def pildyti_degalu(self):
        print("Baterija įkrauta")

    def vaziuoti_autonomiskai(self):
        print("Važiuoja autonomiškai")


elektomobilis = Elektromobilis(2023, "Toyota", "Prius")
elektomobilis.pildyti_degalu()
elektomobilis.vaziuoti_autonomiskai()
print(elektomobilis)

