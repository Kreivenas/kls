import requests

def get_servers(urls):
    print("URL                     Server")
    print("-------------------------------------")

    for url in urls:
        response = requests.head(url)
        server = response.headers.get("Server")
        print(f"{url:<24} {server}")

# Pavyzdys, kaip naudoti funkciją su sąrašu URL
urls = [
    "https://www.delfi.lt/",
    "https://www.alfa.lt/",
    "https://www.15min.lt/",
    "https://www.lrytas.lt/",
    "http://www.google.com/",
    "https://codeacademy.lt/"
]
get_servers(urls)
