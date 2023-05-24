# Sukurkite bazinę klasę pavadinimu "TransportoPriemonė"
# su atributais, tokiais kaip "gamintojas", "modelis" ir "metai".
# Sukurkite po klasę pavadinimu "Automobilis", kuri paveldi nuo "TransportoPriemonės"
# ir prideda papildomą atributą pavadinimu "durų_skaičius".
# Sukurkite "Automobilis" klasės objektą ir išspausdinkite jo atributus. Pvz:
# Make: Toyota
# Model: Camry
# Year: 2022
# Number of doors:

# class TransportoPriemonė:
#     def __init__(self, gamintojas, modelis, metai):
#         self.gamintojas = gamintojas
#         self.modelis = modelis
#         self.metai = metai
#
# class Automobilis(TransportoPriemonė):
#     def durų_skaičius(self):
#         print("5")
#
#     def __str__(self):
#         return f'{self.gamintojas}, {self.modelis}, {self.metai} 5'
#
# mano = Automobilis("BMW", "3", "2023")
# print(mano)
#
# class Figūra:
#     def plotas(self):
#         pass
#
# class Stačiakampis(Figūra):
#     def __init__(self, ilgis, plotis):
#         self.ilgis = ilgis
#         self.plotis = plotis
#
#     def plotas(self):
#         return self.ilgis * self.plotis
#
# class Apskritimas(Figūra):
#     def __init__(self, spindulys):
#         self.spindulys = spindulys
#
#     def plotas(self):
#         return 3.14159 * self.spindulys ** 2
#
# # Sukuriami egzemplioriai ir kviečiamas plotas() metodas
# stačiakampis = Stačiakampis(3, 5)
# apskritimas = Apskritimas(4)
#
# print("Plotas stačiakampio:", stačiakampis.plotas())
# print("Plotas apskritimo:", apskritimas.plotas())
