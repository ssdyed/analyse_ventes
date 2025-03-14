
# 1. Exploration des données
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# commençons par charger les données

fichier = pd.read_excel("/Users/sdye/Desktop/practice/projet1/analyse_ventes/ventes_boutique.xlsx")

# vérifications des infos des données (observer la matrice m x n)
print(fichier.info)

# vérifier les valeurs manquantes
print(fichier.isnull().sum())

# vérifier les valeurs qui arrivent qu'une seule fois par colonne
for col in fichier.columns:
    print(f"{col}: {fichier[col].unique()[:10]}")  # afficher les 10 premières valeurs uniques

# résumé statistiques pour des futurs calculs
print(fichier.describe())

# 2. Analyse des ventes

# le revenu total
revenu_total = fichier["Revenu"].sum
print(f"Le revenu total de cette vente est : {revenu_total} $")

# le produit le plus vendu
quantites_total = fichier.groupby("Produit")["Quantité"].sum()
produit_populaire = quantites_total.idxmax()
quantite_maximale = quantites_total.max()
print(f"Le produit le plus vendu est {produit_populaire} et sa quantité total vendu est de {quantite_maximale} unités.")

# Pour trouver le produit le plus vendu, on peut aussi ordonner les produits en ordre décroissant par leur quantité
produit_decroissant = fichier.groupby("Produit")["Quantité"].sum().sort_values(ascending=False)
print(produit_decroissant)

# La catégorie la plus rentable : elle sera celle avec le plus de revenus après l'accumulation de ses revenus
categorie_rentable = fichier.groupby("Catégorie")["Revenu"].sum().idxmax()
print(f"La catégorie la plus rentable est : {categorie_rentable}.")


# 3. Visualisation des ventes
plt.figure(figsize=(8, 5))
sns.barplot(x=fichier.groupby("Catégorie")["Revenu"].sum().index,  # abscisses
            y=fichier.groupby("Catégorie")["Revenu"].sum().values)  # ordonnées
plt.xticks(rotation=45)  # étiquettes à 45 dégrés
plt.title("Chiffre d'affaires par catégorie")  # titre
plt.show()
