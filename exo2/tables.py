from connexion import get_connection

conn = get_connection()
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS utilisateurs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR (20),
    email VARCHAR (50)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS livres (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titre VARCHAR (20),
    auteur VARCHAR (50)
)
""")

cursor.execute("""
create table if not exists emprunts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_utilisateur INT not null,
    id_livre INT not null,
    date_emprunt DATE,
    date_retour DATE,
    FOREIGN KEY (id_utilisateur) REFERENCES utilisateurs(id),
    FOREIGN KEY (id_livre) REFERENCES livres(id)
)
""")

conn.commit()
conn.close()
print("tables : ok")


