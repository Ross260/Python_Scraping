import requests
from bs4 import BeautifulSoup

# URL d’un livre sur "Books to Scrape"
url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'

# Requête GET pour récupérer le contenu de la page
response = requests.get(url)
if response.status_code != 200:
    print("Erreur lors de la récupération de la page")
    exit()

soup = BeautifulSoup(response.text, 'html.parser')

# Trouver les sections contenant les avis clients
avis_sections = soup.find_all('div', class_='review', limit=5)

# Parcourir les avis et extraire les informations
for avis in avis_sections:
    # Nom du client
    nom_client = avis.find('span', class_='reviewer').get_text(strip=True)
    # Note donnée (ex : 4 étoiles sur 5)
    note = avis.find('span', class_='rating').get_text(strip=True)
    # Commentaire
    commentaire = avis.find('p', class_='review-text').get_text(strip=True)
    # Afficher les informations
    print(f"Nom du client : {nom_client}")
    print(f"Note : {note} étoiles sur 5")
    print(f"Commentaire : {commentaire}\n")
