from bs4 import BeautifulSoup

html = """
<html>
<body>
<h1>Sveiki atvykę į mano tinklalapį</h1>
<p>Ši yra pastraipa.</p>
</body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')
paragraph = soup.find('p').text
print(paragraph)
