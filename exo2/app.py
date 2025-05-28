from gestion_utilisateurs import ajouter_utilisateur
from gestion_livres import ajouter_livre
from gestion_emprunts import enregistrer_emprunt, afficher_emprunts_en_cours, historique_utilisateur

def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Ajouter utilisateur")
        print("2. Ajouter livre")
        print("3. Enregistrer emprunt")
        print("4. Afficher emprunts en cours")
        print("5. Historique utilisateur")
        print("0. Quitter")
        choix = input("Choix : ")

        if choix == "1":
            nom = input("Nom : ")
            email = input("Email : ")
            ajouter_utilisateur(nom, email)
        elif choix == "2":
            titre = input("Titre du livre : ")
            auteur = input("Auteur : ")
            ajouter_livre(titre, auteur)
        elif choix == "3":
            uid = int(input("ID utilisateur : "))
            lid = int(input("ID livre : "))
            enregistrer_emprunt(uid, lid)
        elif choix == "4":
            afficher_emprunts_en_cours()
        elif choix == "5":
            uid = int(input("ID utilisateur : "))
            historique_utilisateur(uid)
        elif choix == "0":
            print("👋 Bye !")
            break
        else:
            print("❌ Choix invalide")

menu ()


