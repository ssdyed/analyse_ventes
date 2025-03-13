import pandas as pd
import matplotlib as plt
import seaborn as sns
import numpy as np

# commençons par charger les données
fichier = pd.read_excel("/Users/sdye/Desktop/practice/ventes_boutique.xlsx")

# on peut aussi afficher que les 7 permières lignes
print(fichier.head(7))

# vérifications des infos des données
print(fichier.info)

# résumé stats
print(fichier.describe())

# vérifier les valeurs manquantes
print(fichier.isnull().sum())
