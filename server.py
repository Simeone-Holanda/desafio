from src.infrastructure.config import Database
from src.applications.CLI import start_service

try:
    Database.set_connection()
    start_service()
except Exception as ex:
    print("Error - ",ex)
    raise ex

