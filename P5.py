from pymongo import MongoClient

# الاتصال
client = MongoClient("mongodb://localhost:27017/")
db = client["info"]
produits = db["produits"]

# ===== CRUD =====

def ajouter_produit():
    nom = input("Nom: ")
    fabriquant = input("Fabriquant: ")
    prix = float(input("Prix: "))

    produits.insert_one({
        "nom": nom,
        "fabriquant": fabriquant,
        "prix": prix
    })

    print("✅ Produit ajouté")


def afficher_produits():
    print("\n📦 Liste des produits:")
    for p in produits.find():
        print(p)


def chercher_produit():
    nom = input("Nom à chercher: ")
    result = produits.find({"nom": {"$regex": nom}})
    
    for p in result:
        print(p)


def modifier_produit():
    nom = input("Nom à modifier: ")
    nouveau_prix = float(input("Nouveau prix: "))

    produits.update_one(
        {"nom": nom},
        {"$set": {"prix": nouveau_prix}}
    )

    print("✏️ Produit modifié")


def supprimer_produit():
    nom = input("Nom à supprimer: ")
    produits.delete_one({"nom": nom})
    print("🗑️ Produit supprimé")


# ===== MENU =====

while True:
    print("\n===== MENU =====")
    print("1 - Ajouter")
    print("2 - Afficher")
    print("3 - Chercher")
    print("4 - Modifier")
    print("5 - Supprimer")
    print("0 - Quitter")

    choix = input("Choix: ")

    if choix == "1":
        ajouter_produit()
    elif choix == "2":
        afficher_produits()
    elif choix == "3":
        chercher_produit()
    elif choix == "4":
        modifier_produit()
    elif choix == "5":
        supprimer_produit()
    elif choix == "0":
        break
    else:
        print("❌ Choix invalide")