import requests
from bs4 import BeautifulSoup

url = "https://orai.15min.lt/prognozes"

# Siunčiame užklausą į puslapį
response = requests.get(url)
r = url.text
print(r)
#
# # Tikriname, ar užklausa buvo sėkminga
# if response.status_code == 200:
#     # Gautame HTML turinį
#     html = response.text
#
#     # Parsiname HTML su BeautifulSoup
#     soup = BeautifulSoup(html, "html.parser")
#
#     # Ieškome temperatūros elemento pagal CSS selektorių
#     temperature_element = soup.select_one("div.city-weather-current-temperature span.temp-c")
#
#     # Tikriname, ar temperatūros elementas buvo rastas
#     if temperature_element:
#         temperature = temperature_element.text
#         print("Dabartinė temperatūra Vilniuje:", temperature)
#     else:
#         print("Nepavyko rasti temperatūros informacijos.")
# else:
#     print("Nepavyko pasiekti puslapio:", url)

