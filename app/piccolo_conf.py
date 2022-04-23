from piccolo.conf.apps import AppRegistry
from piccolo.engine.postgres import PostgresEngine

DB = PostgresEngine(
    config={
        "database": "fhir_pg",
        "user": "admin",
        "password": "admin123",
        "host": "localhost",
        "port": "5432",
    }
)


# A list of paths to piccolo apps
# e.g. ['blog.piccolo_app']
APP_REGISTRY = AppRegistry(apps=["db.piccolo_app"])
