# Turėtų klasę Darbuotojas
# Darbuotojas turėtų savybes: vardas, valandos_ikainis, dirba_nuo
# Turėtų privatų metodą kuris paskaičiuotų,
# kiek darbuotojas nudirbo dienų nuo įvestos dienos (dirba_nuo) iki šiandien
# (turint omeny, kad darbuotojas dirba 7 dienas per savaitę)
# Turėtų metodą paskaiciuoti_atlyginima,
# kuris panaudodamas aukščiau aprašytu metodu, paskaičiuotų bendrą atlyginimą
# (turint omeny, kad darbuotojas dirba 8 valandas per dieną)
# Turėtų klasę NormalusDarbuotojas, kuri pakeistų Darbuotojo klasę taip,
# kad ji skaičiuotų atlyginimą turint omeny, kad darbuotojas dirba 5 dienas per savaitę
# (o ne 7, kaip įprastas darbuotojas).
# Sukurti norimą Darbuotojo objektą
# Sukurti norimą NormalusDarbuotojas objektą
# Su abiem objektais paleisti funkciją paskaiciuoti_atlyginima
from datetime import date, timedelta

class Darbuotojas:
    def __init__(self, vardas, valandos_ikainis, dirba_nuo):
        self.vardas = vardas
        self.valandos_ikainis = valandos_ikainis
        self.dirba_nuo = dirba_nuo

    def _nudirbta_dienų(self):
        dabartinė_data = date.today()
        skirtumas = dabartinė_data - self.dirba_nuo
        return skirtumas.days

    def paskaiciuoti_atlyginima(self):
        dienos = self._nudirbta_dienų()
        užmokestis = dienos * self.valandos_ikainis * 8  # 8 valandos per dieną
        return užmokestis


class NormalusDarbuotojas(Darbuotojas):
    def _nudirbta_dienų(self):
        dienos = super()._nudirbta_dienų()
        savaiciu_skirtumas = dienos // 7
        return dienos - (savaiciu_skirtumas * 2)  # Pašaliname 2 dienas per savaitę



darbuotojas = Darbuotojas("Jonas", 10, date(2022, 1, 1))
normalus_darbuotojas = NormalusDarbuotojas("Petras", 10, date(2022, 1, 1))

atlyginimas_darbuotojas = darbuotojas.paskaiciuoti_atlyginima()
atlyginimas_normalus_darbuotojas = normalus_darbuotojas.paskaiciuoti_atlyginima()

print(f"Darbuotojo atlyginimas: {atlyginimas_darbuotojas}")
print(f"Normalaus darbuotojo atlyginimas: {atlyginimas_normalus_darbuotojas}")
