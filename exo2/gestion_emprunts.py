from connexion import get_connection
from datetime import datetime

def enregistrer_emprunt(id_utilisateur, id_livre):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO emprunts (id_utilisateur, id_livre, date_emprunt, date_retour)
        VALUES (%s, %s, %s, NULL)
    """, (id_utilisateur, id_livre, datetime.today().date()))
    conn.commit()
    conn.close()
    print("✅ Emprunt enregistré.")

def afficher_emprunts_en_cours():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT u.nom, l.titre, e.date_emprunt
        FROM emprunts e
        JOIN utilisateurs u ON e.id_utilisateur = u.id
        JOIN livres l ON e.id_livre = l.id
        WHERE e.date_retour IS NULL
    """)
    for nom, titre, date in cursor.fetchall():
        print(f"📖 {nom} a emprunté « {titre} » le {date}")
    conn.close()

def historique_utilisateur(id_utilisateur):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT l.titre, e.date_emprunt, e.date_retour
        FROM emprunts e
        JOIN livres l ON e.id_livre = l.id
        WHERE e.id_utilisateur = %s
    """, (id_utilisateur,))
    for titre, date_emprunt, date_retour in cursor.fetchall():
        print(f"{titre} | Emprunté le {date_emprunt} | Retour : {date_retour or 'en cours'}")
    conn.close()
