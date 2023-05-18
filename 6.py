def ar_keliamieji_metai(metai):
    if (metai % 4 == 0 and metai % 100 != 0) or metai % 400 == 0:
        return True
    else:
        return False

metai = int(input("Įveskite metus: "))

if ar_keliamieji_metai(metai):
    print(metai, "yra keliamieji metai.")
else:
    print(metai, "nėra keliamieji metai.")
