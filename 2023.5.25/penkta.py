# # Patobulinti objektinio programavimo 1 pamokos biudžeto programą:
#
# Sukurti tėvinę klasę Irasas, kurioje būtų savybės suma , iš kurios klasės PajamuIrasas ir IslaiduIrasas
# paveldėtų visas savybes.
# Į klasę PajamuIrasas papildomai pridėti savybes siuntejas ir papildoma_informacija,
# kurias vartotojas galėtų įrašyti.
# Į klasę IslaiduIrasas papildomai pridėti savybes atsiskaitymo_budas
# ir isigyta_preke_paslauga, kurias vartotojas galėtų įrašyti.
# Atitinkamai perdaryti klasės Biudzetas metodus gauti_balansa
# ir parodyti_ataskaita kad pasiėmus įrašą iš žurnalo, atpažintų,
# ar tai yra pajamos ar išlaidos (pvz., panaudojus isinstance() metodą)
# ir atitinkamai atliktų veiksmus.
# Padaryti, kad vartotojui (per konsolę) būtų leidžiama įrašyti pajamų
# ir išlaidų įrašus, peržiūrėti balansą ir ataskaitą.
class Irasas:
    def __init__(self, suma):
        self.suma = suma

class PajamuIrasas(Irasas):
    def __init__(self, suma, siuntejas, papildoma_informacija):
        super().__init__(suma)
        self.siuntejas = siuntejas
        self.papildoma_informacija = papildoma_informacija

class IslaiduIrasas(Irasas):
    def __init__(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        super().__init__(suma)
        self.atsiskaitymo_budas = atsiskaitymo_budas
        self.isigyta_preke_paslauga = isigyta_preke_paslauga

class Biudzetas:
    def __init__(self):
        self.pajamu_irasai = []
        self.islaidu_irasai = []

    def ivesti_pajamas(self):
        suma = float(input("Įveskite pajamų sumą: "))
        siuntejas = input("Įveskite siuntėją: ")
        papildoma_informacija = input("Įveskite papildomą informaciją: ")
        irasas = PajamuIrasas(suma, siuntejas, papildoma_informacija)
        self.pajamu_irasai.append(irasas)
        print(f"Pajamos {suma} įvestos sėkmingai.")

    def ivesti_islaidas(self):
        suma = float(input("Įveskite išlaidų sumą: "))
        atsiskaitymo_budas = input("Įveskite atsiskaitymo būdą: ")
        isigyta_preke_paslauga = input("Įveskite įsigytą prekę/paslaugą: ")
        irasas = IslaiduIrasas(suma, atsiskaitymo_budas, isigyta_preke_paslauga)
        self.islaidu_irasai.append(irasas)
        print(f"Išlaidos {suma} įvestos sėkmingai.")

    def gauti_balansa(self):
        pajamu_suma = sum(irasas.suma for irasas in self.pajamu_irasai)
        islaidu_suma = sum(irasas.suma for irasas in self.islaidu_irasai)
        balansas = pajamu_suma - islaidu_suma
        print(f"Pajamos: {pajamu_suma} EUR")
        print(f"Išlaidos: {islaidu_suma} EUR")
        print(f"Bendras balansas: {balansas} EUR")

    def parodyti_ataskaita(self):
        print("Biudžeto ataskaita:")
        print("Pajamos:")
        for i, irasas in enumerate(self.pajamu_irasai):
            print(f"Įrašas {i+1}:")
            print(f"  Suma: {irasas.suma} EUR")
            print(f"  Siuntėjas: {irasas.siuntejas}")
            print(f"  Papildoma informacija: {irasas.papildoma_informacija}")
        print("Išlaidos:")
        for i, irasas in enumerate(self.islaidu_irasai):
            print(f"Įrašas {i+1}:")
            print(f"  Suma: {irasas.suma} EUR")
            print(f"  Atsiskaitymo būdas: {irasas.atsiskaitymo_budas}")
            print(f"  Įsigyta prekė/paslauga: {irasas.isigyta_preke_paslauga}")

    def paleisti_programa(self):
        print("=== Mini biudžeto programa ===")
        while True:
            print("\nPasirinkite veiksmą:")
            print("1. Įvesti pajamas")
            print("2. Įvesti išlaidas")
            print("3. Rodyti pajamų/išlaidų balansą")
            print("4. Rodyti biudžeto ataskaitą")
            print("5. Išeiti iš programos")

            pasirinkimas = input("Įveskite pasirinkimo numerį: ")

            if pasirinkimas == "1":
                self.ivesti_pajamas()
            elif pasirinkimas == "2":
                self.ivesti_islaidas()
            elif pasirinkimas == "3":
                self.gauti_balansa()
            elif pasirinkimas == "4":
                self.parodyti_ataskaita()
            elif pasirinkimas == "5":
                print("Programa baigta.")
                break
            else:
                print("Neteisingas pasirinkimas. Bandykite dar kartą.")


biudzetas = Biudzetas()
biudzetas.paleisti_programa()
