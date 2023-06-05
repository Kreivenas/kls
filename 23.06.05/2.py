def ivesties_patikrinimas(patikrinti):
    def zodziai(*args, **kwargs):
        for i in args:
            if type(i) != str:
                 return "Galite ivesti tik teksta!"
        return patikrinti(*args, **kwargs)
    return zodziai

@ivesties_patikrinimas
def Tekstas(*args):
    for tekstas in args:
        print(tekstas)

    return "jusu tekstas"

print(Tekstas("3", 5, "4"))