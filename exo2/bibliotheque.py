#pour la connexion a la base de donnée il est necessaire d'importer (installer :  pip install mysql-connector-python ) mysql-connector-python (lien entre python et bdd)
import mysql.connector
# chargé variable d'environnement (installer: python-dotenv)
from dotenv import load_dotenv
import os
#charger les variables d'environnements du fichier .env
load_dotenv()