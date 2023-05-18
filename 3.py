def ar_palindromas(zodis):
    zodis = zodis.lower().replace(" ", "")
    return zodis == zodis[::-1]

sarasas = ["ėmė", "savas", "alus", "kolkas",
           "12321", "labas", "level", "python",
           "Madam", "12321", "racecar"]

for zodis in sarasas:
    if ar_palindromas(zodis):
        print(zodis, "yra palindromas")
    else:
        print(zodis, "nėra palindromas")
