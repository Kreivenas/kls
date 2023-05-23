import datetime

class Sukaktis:
    def __init__(self, metai, menesis, diena, valanda, minute):
        self.data = datetime.datetime(metai, menesis, diena, valanda, minute)

    def praėjo_laiko(self):
        dabar = datetime.datetime.now()
        skirtumas = dabar - self.data

        metu_skirtumas = skirtumas.days // 365
        savaites_skirtumas = skirtumas.days // 7
        dienos_skirtumas = skirtumas.days
        valandos_skirtumas = skirtumas.seconds // 3600
        minutes_skirtumas = (skirtumas.seconds // 60) % 60
        sekundes_skirtumas = skirtumas.seconds % 60

        print(f"Praėjo: {metu_skirtumas} metų, {savaites_skirtumas} savaičių, {dienos_skirtumas} dienų, {valandos_skirtumas} valandų, {minutes_skirtumas} minučių, {sekundes_skirtumas} sekundžių")

    def arKeliamieji(self):
        return self.data.year % 4 == 0 and (self.data.year % 100 != 0 or self.data.year % 400 == 0)

    def atimti_dienas(self, dienos):
        nauja_data = self.data - datetime.timedelta(days=dienos)
        return nauja_data

    def pridėti_dienas(self, dienos):
        nauja_data = self.data + datetime.timedelta(days=dienos)
        return nauja_data

# Testavimas
data1 = Sukaktis(2000, 1, 1, 12, 12)
data1.praėjo_laiko()
print(data1.arKeliamieji())
print(data1.atimti_dienas(10))
print(data1.pridėti_dienas(5))
