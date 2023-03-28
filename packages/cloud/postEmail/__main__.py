import os
from pymongo import MongoClient

def main(args):
    client = MongoClient(os.environ['DATABASE_URL'])
    db = client['do-coffee']

    try:
        db['email-list'].insert_one({
            'subscriber': args['email'],
        })
        return {
            'ok': True
        }
    except Exception as err:
        return {
            'body': {
                'error': "There was a problem adding the email address to the "
                         "database." 
            },
            "statusCode": 400
        }