from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Lancer le navigateur Chrome
driver = webdriver.Chrome()

# Ouverture du moteur de recherche et Airbnb
driver.get("https://www.airbnb.fr/")
time.sleep(3)

# Remplir la barre de recherche
search_box = driver.find_element(By.XPATH, '//input[@placeholder="Rechercher une destination"]')
search_box.send_keys("Paris")
time.sleep(1)
search_box.send_keys(Keys.RETURN)
time.sleep(5)

# Attendre que la liste des résultats soit visible
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//div[@itemprop="itemListElement"]'))
)

# Récupérer les 5 premiers résultats
listings = driver.find_elements(By.XPATH, '//div[@itemprop="itemListElement"]')

if len(listings) >= 5:
    listings = listings[:5]
else:
    print("Moins de 5 résultats trouvés !")

# Affichage des résultats sous forme de tableau
print("\n" + "=" * 60)
print(f"| {'#':^3} | {'Titre / Description':^40} | {'Prix':^10} |")
print("=" * 60)

for i, listing in enumerate(listings, 1):
    text = listing.text.split("\n")

    # Récupérer les données importantes (à adapter si besoin)
    titre = text[0] if len(text) > 0 else "N/A"
    prix = text[-1] if len(text) > 1 else "N/A"

    # Affichage formaté en tableau
    print(f"| {i:^3} | {titre[:40]:40} | {prix:10} |")

print("=" * 60)

# Fermeture du navigateur
driver.quit()
