
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# les deux bibliothèques pour l'attente du chargement des infos de la pages
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Chemin du ChromeDriver (remplace avec ton chemin)
CHROME_DRIVER_PATH = '/path/to/chromedriver'

# Lancer le navigateur Chrome
driver = webdriver.Chrome()

# Ouvrir une page web
driver.get("https://www.google.com")

# Ouvrir Airbnb
driver.get("https://www.airbnb.fr/")
time.sleep(3)  # Laisser le site se charger

# Remplir la barre de recherche
search_box = driver.find_element(By.XPATH, '//input[@placeholder="Rechercher une destination"]')
search_box.send_keys("Paris")
time.sleep(1)
search_box.send_keys(Keys.RETURN)
time.sleep(5)  # Attendre le chargement des résultats

# -------------------------------------------------------------------------------------------------
# Attendre que la liste des résultats soit visible
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//div[@itemprop="itemListElement"]'))
)

# Récupérer les 5 premiers résultats
listings = driver.find_elements(By.XPATH, '//div[@itemprop="itemListElement"]')

# Vérifier qu'on a bien trouvé au moins 5 résultats
if len(listings) >= 5:
    listings = listings[:5]  # Sélectionner les 5 premiers
else:
    print(" Moins de 5 résultats trouvés !")

print("Top 5 logements Airbnb à Paris :")

# Afficher les résultats
for i, listing in enumerate(listings, 1):
    print(f"Résultat {i}: {listing.text}")  # Affiche le texte du bloc trouvé
    print(" ")
# ---------------------------------------------------------------------------------------------

# Fermer le navigateur
driver.quit()
