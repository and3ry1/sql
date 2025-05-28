from connexion import get_connection

def ajouter_livre(titre, auteur):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO livres (titre, auteur) VALUES (%s, %s)", (titre, auteur))
    conn.commit()
    
    print ("livre ajouté avec l'ID:", cursor.lastrowid)

    conn.close()
    