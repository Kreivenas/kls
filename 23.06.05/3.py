def kartojimas(kartai):
    def kartoti(func):
        def wrapper():
            for i in range(kartai):
                func()
        return wrapper
    return kartoti

@kartojimas(kartai=3)
def spausdinti_teksta():
    print("Spausdinamas tekstas!")


spausdinti_teksta()