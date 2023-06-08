import random

# Delfi antraščių sąrašas
antrasciu_sarasas = [
    "Orai: už 9 šlakius teks sumokėti 26 tūkstančius eurų",
    "Antradienio vakare kauniečius išgąsdino termofikacijos elektrinė: ar bus naujagimių bumas?",
    "Koronavirusas atakuoja: rekordinės mirties skaičius",
    "Skaandalas politiko šeimoje: pasikėlė pavojus sveikatai",
    "Naujasis mokslinis tyrimas: COVID-19 gali plisti oro lašeliniu būdu"
]

# Blogų žodžių sąrašas
blogi_zodziai = ["COVID", "mirtis"]

# Tuščios sąrašų pirmoje ir antroje dalyje
pirmoji_dalis = []
antroji_dalis = []

# Tikriname antraštes ir sudedame jas į atitinkamus sąrašus
for antraste in antrasciu_sarasas:
    if ":" in antraste:
        dalys = antraste.split(":")
        pirmoji_dalis.append(dalys[0])
        antroji_dalis.append(dalys[1])
    else:
        pirmoji_dalis.append(antraste)
        antroji_dalis.append("")

# Išmaišome antrojo sąrašo elementus
random.shuffle(antroji_dalis)

# Filtruojame antrastes pagal blogus žodžius
filtruotos_antrasciu_sarasas = []
for i in range(len(pirmoji_dalis)):
    blogi_zodziu_rasta = False
    for zodis in blogi_zodziai:
        if zodis.lower() in pirmoji_dalis[i].lower() or zodis.lower() in antroji_dalis[i].lower():
            blogi_zodziu_rasta = True
            break
    if not blogi_zodziu_rasta:
        filtruotos_antrasciu_sarasas.append(pirmoji_dalis[i] + ": " + antroji_dalis[i])

# Spausdiname rezultatus
for antraste in filtruotos_antrasciu_sarasas:
    print(antraste)
