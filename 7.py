from datetime import datetime

def dienu_skirtumas(pirmoji_data, antroji_data):
    skirtumas = (antroji_data - pirmoji_data).days
    return abs(skirtumas)

pirmoji_data = datetime.strptime(input("Įveskite pirmąją datą (yyyy-mm-dd): "), "%Y-%m-%d")
antroji_data = datetime.strptime(input("Įveskite antrąją datą (yyyy-mm-dd): "), "%Y-%m-%d")

skirtumo_dienos = dienu_skirtumas(pirmoji_data, antroji_data)

print("Dienų skirtumas tarp dviejų datų:", skirtumo_dienos)
