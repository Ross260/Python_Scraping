import pandas as pd

# Charger le fichier CSV dans un DataFrame Pandas
df = pd.read_csv("CSV_Files/ventes.csv")
print(df.head())

print(df.duplicated().sum())

print(df.drop_duplicates())
newdf = df.drop_duplicates() # pour enregistrer le nouveau df sans produit dupliquer
newdf.to_csv("CSV_Files/ventes.csv")



#Exo 1
"""
import pandas as pd

# Charger le fichier CSV dans un DataFrame Pandas
data = pd.read_csv("CSV_Files/data1.csv")
print(data.head())
df = pd.DataFrame(data)
valeurs_manquantes = df.isnull().sum()

moyenne_revenu = df['revenu'].mean()

# Afficher le nombre de valeurs manquantes par colonne
valeurs_manquantes = df.isnull().sum()
print("Nombre de valeurs manquantes par colonne :\n", valeurs_manquantes)

# Supprimer les lignes contenant des valeurs manquantes
df_sans_nan = df.dropna()

# Remplacer les valeurs NaN de la colonne revenu par la moyenne de la colonne
moyenne_revenu = df['revenu'].mean()
#df['revenu'].fillna(moyenne_revenu, inplace=True)
df.fillna({'revenu': moyenne_revenu}, inplace=True)  # syntaxe proposer par pycharm pour resoudre l'erreur

# Sauvegarder le DataFrame nettoyé dans un fichier data1_cleaned.csv
df_sans_nan.to_csv('nettoyage/data1_cleaned.csv', index=False)
print("DataFrame nettoyé sauvegardé dans 'data1_cleaned.csv'")
"""