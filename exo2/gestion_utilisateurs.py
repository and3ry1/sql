from connexion import get_connection

def ajouter_utilisateur(nom, email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute ("INSERT INTO utilisateurs (nom, email) VALUES (%s,%s)",  (nom, email))
    conn.commit()
    print ("utilisateur ajout avec l'ID:", cursor.lastrowid) 
    conn.close()
    
