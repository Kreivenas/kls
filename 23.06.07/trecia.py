import requests

def get_weather_forecast():
    url = "https://orai.15min.lt/prognozes"

    response = requests.get(url)
    if response.ok:
        html_content = response.text

        # Ieškome žymės, kurioje yra oro prognozė Vilniuje
        start_tag = "<div class=\"temperature alert-hot\">"
        end_tag = '</p>'

        start_index = html_content.find(start_tag)
        end_index = html_content.find(end_tag, start_index)

        if start_index != -1 and end_index != -1:
            forecast = html_content[start_index + len(start_tag):end_index]
            print(f"Oro prognozė Vilniuje: {forecast.strip()}")
        else:
            print("Nepavyko rasti oro prognozės.")
    else:
        print("Nepavyko gauti tinklalapio duomenų.")

# Paleidžiame funkciją
get_weather_forecast()

