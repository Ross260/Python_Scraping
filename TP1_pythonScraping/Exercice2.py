import requests
from bs4 import BeautifulSoup

# URL de la page avec le classement de la Premier League
url = "https://www.bbc.com/sport/football/premier-league/table"
response = requests.get(url)
# Vérifier que la requête a réussi (code HTTP 200)
if response.status_code == 200:

    soup = BeautifulSoup(response.text, 'html.parser')
    # Pour trouver le tableau contenant le classement des équipes de Premier League
    table = soup.find('table')
    # Vérifions si la table a été trouvée
    if table:
        # Pour prendre les les dix premières équipe du classement
        rows = table.find_all('tr')[1:11]
        # Afficher les résultats sous forme de tableau
        print(f"{'Position':<10} {'Équipe':<30} {'Points':<10} {'Victoires':<10} {'Défaites':<10}")
        print("=" * 70)
    for row in rows:

        cols = row.find_all('td')
        if len(cols) > 4:
            # Extraire les informations nécessaires
            position = cols[0].get_text().strip()
            team = cols[1].get_text().strip()
            points = cols[2].get_text().strip()
            wins = cols[3].get_text().strip()
            losses = cols[4].get_text().strip()
            # Affichons les données sous forme de tableau
            print(f"{position:<10} {team:<30} {points:<10} {wins:<10} {losses:<10}")
        else:
            print("Tableau non trouvé.")
else:
    print("Erreur.")
