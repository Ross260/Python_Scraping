import requests
from bs4 import BeautifulSoup

# URL de la recette Blanquette de veau facile
url = 'https://www.marmiton.org/recettes/recette_blanquette-de-veau-facile_19219.aspx'

# Faire la requête HTTP pour obtenir la page
response = requests.get(url)
response.raise_for_status()  # Vérifier que la requête a bien réussi

# Parser le contenu de la page avec BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Essayer de récupérer le titre de la recette
title = soup.find('div', class_='main-title').find('h1')
if title:
    title = title.text.strip()
else:
    title = "Titre non trouvé"

# Extraire les ingrédients en utilisant la classe 'card-ingredient'
ingredients = soup.find_all('div', class_='card-ingredient')

# Extraire les étapes de préparation
steps = soup.find_all('div', class_='recipe-step-list__container')

# Affichage des résultats
print(f"Titre de la recette : {title}\n")

print("Ingrédients :")
for ingredient in ingredients:
    ingredient_name = ingredient.get('data-name', 'Ingrédient non trouvé')
    print(f"- {ingredient_name}")

print("\nÉtapes de préparation :")
for idx, step in enumerate(steps, 1):
    step_text = step.find('p').text.strip()  # Extraire le texte de chaque étape
    print(f"Étape {idx}: {step_text}")