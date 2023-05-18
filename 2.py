def gauti_ilgiausia_zodi(is_failo):
    ilgiausias_zodis = ''

    with open(is_failo, 'r') as failas:
        turinys = failas.read()
        zodziai = turinys.split()

        for zodis in zodziai:
            if len(zodis) > len(ilgiausias_zodis):
                ilgiausias_zodis = zodis

    return ilgiausias_zodis


failo_kelias = input("Įveskite failo kelią/pavadinimą: ")
ilgiausias = gauti_ilgiausia_zodi(failo_kelias)
ilgis = len(ilgiausias)

print("Ilgiausias žodis:", ilgiausias, "Jo ilgis:", ilgis )
print("Jo ilgis:", ilgis)
