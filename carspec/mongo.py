from pymongo import MongoClient
import os

client = MongoClient(os.environ.get('MONGO_LOCAL'))

def saveToMongo(carSpec,database,collection):

    db = client.get_database(database)
    db[collection].insert(carSpec)




