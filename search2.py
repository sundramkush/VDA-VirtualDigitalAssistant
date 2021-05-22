from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()



def searchInElasticSearch(problem_name):
    li=[]   
    search_param = {
        "query":{
            "match":{
                "problem_name":{
                    "query": problem_name,
                    "fuzziness":"2"
                    }
                }
            }
        }
    
    d = es.search(index='vda2',body=search_param)
    for a in d["hits"]["hits"]:
        li.append(a["_source"]["problem_name"])
        
    print(li)
    return li

searchInElasticSearch("strn")

