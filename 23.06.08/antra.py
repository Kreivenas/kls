from bs4 import BeautifulSoup

html = '''
<html>
<body>
<a href="https://www.example.com">Nuoroda 1</a>
<a href="https://www.google.com">Nuoroda 2</a>
<a href="https://www.github.com">Nuoroda 3</a>
<a href="https://www.codeacademi.lt">Nuoroda 4</a>

</body>
</html>
'''

soup = BeautifulSoup(html, 'html.parser')
links = soup.find_all('a')

for link in links:
    href = link.get('href')
    text = link.text
    print(f"Nuoroda: {href} - Tekstas: {text}")
