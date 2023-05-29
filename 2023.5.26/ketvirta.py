from datetime import datetime

class Kursas:
    def __init__(self, pavadinimas, paskaitu_skaicius, valandos, data):
        self.pavadinimas = pavadinimas
        self.paskaitu_skaicius = paskaitu_skaicius
        self.valandos = valandos
        self.data = self._patikrinti_data(data)
        self.atšauktos_dienos = []

    def _patikrinti_data(self, data):
        if data.year < 2023:
            print(f"Keičiami metai į 2024: {data}")
            data = data.replace(year=2024)
        return data

    def prideti_atšaukta_diena(self, atšaukta_data):
        self.atšauktos_dienos.append(atšaukta_data)

    def gauti_kurso_duomenis(self):
        return f"Kursas: {self.pavadinimas}\n" \
               f"Paskaitų skaičius: {self.paskaitu_skaicius}\n" \
               f"Paskaitos valandos: {self.valandos}\n" \
               f"Kurso data: {self.data}\n" \
               f"Atšauktos dienos: {self.atšauktos_dienos}"


# Pavyzdys kaip naudoti Kursas klasę

# Sukuriame naują Kursas objektą
kursas1 = Kursas("Programavimas", 10, "2h", datetime(2023, 3, 15))
print(kursas1.gauti_kurso_duomenis())

# Pridedame atšauktą dieną
kursas1.prideti_atšaukta_diena(datetime(2023, 4, 4))
print(kursas1.gauti_kurso_duomenis())

# Sukuriame kitą Kursas objektą su ankstyvesne data
kursas2 = Kursas("Dizainas", 8, "1.5h", datetime(2021, 12, 5))
print(kursas2.gauti_kurso_duomenis())
