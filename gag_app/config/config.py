AUTH_USER = 'gadmin48'  # user name to whom media creation will be attributed.
# for instance an admin account.

GAG_BASE_LANGUAGE = 'fr'  # main language of GAG database


SOURCES = [
    {
        "AUTHENT_STRUCTURE": 'PNC',
        "GADMIN_BASE_URL": 'geotrek-admin.cevennes-parcnational.net',
        "DATA_TO_IMPORT": ['Trek', 'POI'],
        "PORTALS": ['DEP_48'],
    },
    {
        "AUTHENT_STRUCTURE": 'PNE',
        "GADMIN_BASE_URL": 'geotrekdemo.ecrins-parcnational.fr',
        "DATA_TO_IMPORT": ['Trek', 'POI'],
        "PORTALS": None,
    },
    {
        "AUTHENT_STRUCTURE": 'Conseil départemental de la Lozère',
        "GADMIN_BASE_URL": 'admin48.openig.org',
        "DATA_TO_IMPORT": ['Trek', 'POI'],
        "PORTALS": None,
    },
    {
        "AUTHENT_STRUCTURE": 'PNRGCA',
        "GADMIN_BASE_URL": 'openig-geotrek-pnrgca.ataraxie.fr',
        "DATA_TO_IMPORT": ['Trek', 'POI'],
        "PORTALS": ['Rando Lozère'],
    },
]

## AUTHENT_STRUCTURE:
# Used to attribute aggregate data to a specific structure in GAG database.
# Should match a line in "authent_structure" GAG table.
# Essential for data traceability.
# /!\ It's not a filter on imported data!
# It isn't used to query source API,
# thus it doesn't rely on source Geotrek-admin's structures.

## GADMIN_BASE_URL:
# Source Geotrek-admin's URL

## DATA_TO_IMPORT:
# List of the Django models' names of the data we want to import from this source

## PORTALS:
# If needed, name of source database's portal(s)
# from which we want to get data. Can be set to None
