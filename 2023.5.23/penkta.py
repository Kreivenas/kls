class Biudzetas:
    def __init__(self):
        self.pajamos = []
        self.islaidos = []

    def ivesti_pajamas(self):
        suma = float(input("Įveskite pajamų sumą: "))
        self.pajamos.append(suma)
        print(f"Pajamos {suma} įvestos sėkmingai.")

    def ivesti_islaidas(self):
        suma = float(input("Įveskite išlaidų sumą: "))
        self.islaidos.append(suma)
        print(f"Išlaidos {suma} įvestos sėkmingai.")

    def balansas(self):
        pajamu_suma = sum(self.pajamos)
        islaidu_suma = sum(self.islaidos)
        balansas = pajamu_suma - islaidu_suma
        print(f"Pajamos: {pajamu_suma} EUR")
        print(f"Išlaidos: {islaidu_suma} EUR")
        print(f"Bendras balansas: {balansas} EUR")

    def biudzeto_ataskaita(self):
        print("Biudžeto ataskaita:")
        print("Pajamos:")
        for i, suma in enumerate(self.pajamos):
            print(f"Įrašas {i+1}: {suma} EUR")
        print("Išlaidos:")
        for i, suma in enumerate(self.islaidos):
            print(f"Įrašas {i+1}: {suma} EUR")

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
                self.balansas()
            elif pasirinkimas == "4":
                self.biudzeto_ataskaita()
            elif pasirinkimas == "5":
                print("Programa baigta.")
                break
            else:
                print("Neteisingas pasirinkimas. Bandykite dar kartą.")


# Paleidžiame programą
biudzetas = Biudzetas()
biudzetas.paleisti_programa()
