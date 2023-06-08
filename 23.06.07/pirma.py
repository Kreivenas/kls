import requests

def kates_fot(kiekis):
    url = "https://cataas.com/cat"

    for i in range(kiekis):
        response = requests.get(url)
        with open(f"kate{i + 1}.jpg", "wb") as file:
            file.write(response.content)
            print(f"Kates Nuotrauka {i + 1} isaugota.")

kates_fot(3)
