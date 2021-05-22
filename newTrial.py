from pymongo import MongoClient
from elasticsearch import Elasticsearch
from tqdm import tqdm


mgclient = MongoClient("mongodb://localhost:27017/")
db = mgclient['vda2']
col = db['videos2']

es1 = Elasticsearch()


# Defining a custom exception
class UnsupportedTypeError(Exception):
    pass

#%% tHE CRUD oPERATIONS

# Inserting in ElasticSearch
def enterInElasticSearch(data):
    data.pop('_id')
    # action = {
    #         "index": {
    #                 "_index": 'vda',
    #                 "_type": 'video',
    #                 }
    # }
    es1.index(index = 'vda2', body = data, refresh = True)

# Inserting in MongoDB
def enterInMongoDB(data):
    try:
        if type(data["keywords"])!=list : raise UnsupportedTypeError
        col.insert_one(data)
        enterInElasticSearch(data)
        
    except UnsupportedTypeError:
        print("Keywords must be a list")
        
enterInMongoDB({"problem_name":"amstrong number","keywords":["cube","add","multipy","same","compare","number","equal","python"]})
        