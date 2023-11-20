"""
Binette book !
"""


import os
import logging
import dotenv           # pip install python-dotenv

from flask import Flask, render_template

import bd
from mur import bp_mur
from compte import bp_compte

# Doit être fait avant de démarrer l'application pour charger les variables d'environnement
if not os.getenv('BD_UTILISATEUR'):
    dotenv.load_dotenv('.env')

app = Flask(__name__)

app.logger.setLevel(logging.DEBUG)

app.register_blueprint(bp_mur, url_prefix='/mur')
app.register_blueprint(bp_compte, url_prefix='/compte')


# Faire la commande suivante pour générer une chaîne aléatoire :
# python -c "import secrets; print(secrets.token_hex())"
app.secret_key = os.getenv("SECRET_SESSION")


@app.route('/')
def index():
    """Affiche l'accueil"""
    app.logger.info("Affichage des utilisateurs")
    with bd.creer_connexion() as conn:
        utilisateurs = bd.get_utilisateurs(conn)
    return render_template('index.jinja', utilisateurs=utilisateurs)


if __name__ == '__main__':
    app.run(debug=True)
