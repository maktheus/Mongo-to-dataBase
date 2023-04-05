import pymongo


def ConnectToMongoDataBase(url, db, collection):
    # Conectar ao banco de dados
    client = pymongo.MongoClient(url)
    db = client[db]
    collection = db[collection]

    return collection
