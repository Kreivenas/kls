class staciakampis:
    def __init__(self, plotis, aukstis):
        self.plotis = plotis
        self.aukstis = aukstis

    def plotas(self):
        return self.plotis * self.aukstis
    def perimetras(self):
        return (self.plotis + self.aukstis) * 2

st = staciakampis(5, 7)


plotas = st.plotas()
print(plotas)
perimetras = st.perimetras()
print(perimetras)




