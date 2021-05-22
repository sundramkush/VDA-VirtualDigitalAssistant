# The total integration of the Virtual Doubt Assistance
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from pymongo import MongoClient
import vidToAud as v

client = MongoClient("mongodb://localhost:27017/")
db=client.VDA
mycol=db.DOC
#mydict = {"id" : "Python_For_Loops"}
#mycol.delete_one(mydict)
#for x in mycol.find():
 #   print(x)
  #  if fuzz.token_set_ratio("make",x["keywords"])>30 : print(x["id"])

text = v.vidToAud("Video.mp4")
content = v.theProcessing("Video", text)
print(content)

mydict = {"id": content["id"], "keywords": content["keywords"]}
mycol.insert_one(mydict)
