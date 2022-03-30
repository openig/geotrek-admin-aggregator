API_BASE_URL = 'https://geotrekdemo.ecrins-parcnational.fr/api/v2/' ## URL de l'API v2 de la base de données source
AUTHENT_STRUCTURE = 'PNE' ## Nom de la source des données. Doit correspondre à une entrée dans la table "authent_structure". Indispensable pour la tracabilité des données.
SQLALCHEMY_DATABASE_URI = 'postgresql://geotrek:geotrek@91.206.199.188:5432/geotrekdb' ## URI de la base de données aggregator, au format SQLAlchemy
GAG_BASE_LANGUAGE = 'fr' ## langue par défaut de la base de données aggregator
SRID = 2154 ## SRID du système de coordonnées de la base de données aggregator

SQLALCHEMY_TRACK_MODIFICATIONS = False ## Désactive le suivi des modifications de la part de SQLAlchemy
