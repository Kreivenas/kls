import requests  # importuojame requests
from time import time  # importuojame time modulį
#
# start_time = time()  # fiksuojame starto laiką
# r = requests.get('http://www.cnn.com')  # sukuriame http užklausą
# print(r.status_code)  # spausdiname status code (200 = OK, 404 = Not Found, ir t.t. galima pasiguglinti http status codes)
# end_time = time()  # fiksuojame pabaigos laiką
# print(end_time - start_time)  # atspausdiname laiką, per kurį gaovme atsakymą


def matuoti_laika(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print("Funkcija:", func.__name__)
        print("Atsakymas:", result)
        print("Iš viso užtruko:", end_time - start_time, "sekundžių")
        return result
    return wrapper

@matuoti_laika
def siusti_uzklausa(url):
    r = requests.get(url)
    return r.status_code

url = 'http://www.cnn.com'
siusti_uzklausa(url)
