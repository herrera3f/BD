from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId


url = "mongodb+srv://brandonmarin02:Bsmh7700@database.8gmwdpo.mongodb.net/?retryWrites=true&w=majority"


def conexion():
    cliente = MongoClient(url,Server_Api=ServerApi('1'))
    try:
        cliente.admin.command('ping')
        db = cliente.universidad
        return db
    
    except Exception as e:
        print(e)

