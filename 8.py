def skaiciu_dalyba(sk1, sk2):
    try:
        rezultatas = sk1 / sk2
        return rezultatas
    except ZeroDivisionError:
        print("Dalyba iš nulio negalima!")
        return None

while True:
    try:
        skaicius1 = int(input("Įveskite pirmąjį skaičių: "))
        skaicius2 = int(input("Įveskite antrąjį skaičių: "))
        break
    except ValueError:
        print("Neteisinga įvestis! Prašome įvesti sveikąjį skaičių.")

rezultatas = skaiciu_dalyba(skaicius1, skaicius2)

if rezultatas is not None:
    print("Dalybos rezultatas:", rezultatas)
