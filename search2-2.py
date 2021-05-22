from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()



def searchInElasticSearch(problem_name):
    li=[]   
    search_param = {
        "query":{
            "fuzzy":{
                "problem_name":{
                    "value":problem_name
                    }
                }
            }
        }
    
    d = es.search(index='vda',body=search_param)
    for a in d["hits"]["hits"]:
        li.append(a["_source"]["problem_name"])
        
    return li
