import os
from pymongo import MongoClient

def main():
    client = MongoClient(os.environ['DATABASE_URL'])
    db = client['do-coffee']
    inventory = list(db['available-coffees'].find({}, {'_id': 0}))
    print(inventory)
    
    return {
        'body': inventory,
    }