from pymongo import MongoClient
from elasticsearch import Elasticsearch
from tqdm import tqdm


mgclient = MongoClient("mongodb://localhost:27017/")
db = mgclient['vda']
col = db['video']

es1 = Elasticsearch()


# Defining a custom exception
class UnsupportedTypeError(Exception):
    pass

#%% tHE CRUD oPERATIONS

# Inserting in ElasticSearch
def enterInElasticSearch(data):
    # action = {
    #         "index": {
    #                 "_index": 'vda',
    #                 "_type": 'video',
    #                 }
    # }
    es1.index(index = 'vda', body = data, refresh = True)

# Inserting in MongoDB
def enterInMongoDB(data):
    try:
        if type(data["keywords"])!=list : raise UnsupportedTypeError
        col.insert_one(data)
        enterInElasticSearch(data)
        
    except UnsupportedTypeError:
        print("Keywords must be a list")
        
enterInElasticSearch({"problem_name":"Palindrome or a simple string","keywords":[1,2,3,4,5]})
        