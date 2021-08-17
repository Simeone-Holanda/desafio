from src.infrastructure.config import Database
from src.applications.CLI import import_csv
from src.app import app

try:
    Database.set_connection()
    #import_csv()
    app.run(port=8000)
except Exception as ex:
    print("Error - ",ex)
    raise ex

