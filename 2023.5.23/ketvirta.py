class Studentas:
    def __init__(self, vardas, amzius, lytis):
        self.vardas = vardas
        self.amzius = amzius
        self.lytis = lytis

class Kursas:
    def __init__(self, pavadinimas):
        self.pavadinimas = pavadinimas
        self.studentai = []

    def prideti_studenta(self, studentas):
        self.studentai.append(studentas)

# Testavimas
studentas1 = Studentas("Jonas", 20, "Vyras")
studentas2 = Studentas("Ona", 22, "Moteris")

kursas = Kursas("Programavimas")
kursas.prideti_studenta(studentas1)
kursas.prideti_studenta(studentas2)

for studentas in kursas.studentai:
    print(f"Studentas: {studentas.vardas}, Amžius: {studentas.amzius}, Lytis: {studentas.lytis}")
