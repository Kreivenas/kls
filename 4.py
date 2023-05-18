import pickle

def prideti_preke(krepselis):
    pavadinimas = input("Įveskite prekės pavadinimą: ")
    kaina = float(input("Įveskite prekės kainą: "))
    krepselis[pavadinimas] = kaina
    print("Prekė pridėta į krepšelį.")

def istrinti_preke(krepselis):
    pavadinimas = input("Įveskite prekės pavadinimą, kurią norite pašalinti: ")
    if pavadinimas in krepselis:
        del krepselis[pavadinimas]
        print("Prekė pašalinta iš krepšelio.")
    else:
        print("Tokia prekė neegzistuoja krepšelyje.")

def perziureti_prekes(krepselis):
    if not krepselis:
        print("Krepšelis tuščias.")
    else:
        print("Krepšelyje esančios prekės:")
        for pavadinimas, kaina in krepselis.items():
            print(f"Pavadinimas: {pavadinimas}, Kaina: {kaina}")

def bendra_suma(krepselis):
    suma = sum(krepselis.values())
    print(f"Bendra krepšelio suma: {suma}")

def saugoti_krepseli(krepselis, failo_pavadinimas):
    with open(failo_pavadinimas, 'wb') as failas:
        pickle.dump(krepselis, failas)
    print("Krepšelis išsaugotas į failą.")

def uzkrauti_krepseli(failo_pavadinimas):
    with open(failo_pavadinimas, 'rb') as failas:
        krepselis = pickle.load(failas)
    return krepselis

def meniu():
    krepselis = {}
    failo_pavadinimas = "krepšelis.pkl"

    while True:
        print("\nPasirinkite veiksmą:")
        print("1. Pridėti prekę į krepšelį")
        print("2. Pašalinti prekę iš krepšelio")
        print("3. Peržiūrėti krepšelio prekes")
        print("4. Peržiūrėti bendrą krepšelio sumą")
        print("5. Išsaugoti krepšelį į failą")
        print("6. Užkrauti krepšelį iš failo")
        print("0. Baigti programą")

        pasirinkimas = input("Įveskite pasirinkimo numerį: ")

        if pasirinkimas == "1":
            prideti_preke(krepselis)
        elif pasirinkimas == "2":
            istrinti_preke(krepselis)
        elif pasirinkimas == "3":
            perziureti_prekes(krepselis)
        elif pasirinkimas == "4":
            bendra_suma(krepselis)
        elif pasirinkimas == "5":
            saugoti_krepseli(krepselis, failo_pavadinimas)
        elif pasirinkimas == "6":
            krepselis = uzkrauti_krepseli(failo_pavadinimas)
            print("Krepšelis užkrautas iš failo.")
        elif pasirinkimas == "0":
            break
        else:
            print("Netinkamas pasirinkimas, bandykite dar kartą.")

meniu()
