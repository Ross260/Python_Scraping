import requests
from bs4 import BeautifulSoup

# extraction des citations sur la page
# Accédons à la page web
url = "http://quotes.toscrape.com/"
response = requests.get(url)

# Vérifier que la requête a réussi (code HTTP 200)
if response.status_code == 200:
    # Extraire le contenu de la page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Trouvons toutes les citations sur la page
    quotes = soup.find_all('div', class_='quote')
    # On récupere les 10 premières citations avec les auteurs
    for i, quote in enumerate(quotes[:10]):
        text = quote.find('span', class_='text').get_text() # Citation
        author = quote.find('small', class_='author').get_text() # Auteur
        print(f'"{text}" - {author}')
else:
    print("Erreur.")