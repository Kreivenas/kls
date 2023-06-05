def skaiciu_padavimas(patikrinti):
    def skaiciai(*args, **kwargs):
        if len(args) > 2:
            return "Perdaug Skaiciu!"
        return patikrinti(*args, **kwargs)
    return skaiciai

@skaiciu_padavimas
def Dauginti(*args):
    rezultatas = 1
    for skaicius in args:
        rezultatas *= skaicius
    return rezultatas

print(Dauginti(3, 4))