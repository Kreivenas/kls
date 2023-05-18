import re


def skaiciuoti_zodzius(tekstas):
    zodziu_skaicius = {}
    zodziai = re.findall(r'\b\w+\b', tekstas.lower())

    for zodis in zodziai:
        if zodis in zodziu_skaicius:
            zodziu_skaicius[zodis] += 1
        else:
            zodziu_skaicius[zodis] = 1

    return zodziu_skaicius


tekstas = input("Įveskite tekstą: ")
rezultatas = skaiciuoti_zodzius(tekstas)
print(rezultatas)
