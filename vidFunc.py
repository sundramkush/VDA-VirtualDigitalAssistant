import os
import vidToAud as v
import time


st = time.time()

videosContent=[]

vidNames = os.listdir(r"D:\Ram\Internship\Virtual Doubt Assistant\Take 2\Videos")


for name in vidNames:
    text=v.vidToAud(name.split('.')[0],name.split('.')[0].replace(" ",""))
    print(name.split('.')[0],"\n\n")
    v.theProcessing(name.split('.')[0],text)
    
    
print("The total time is ",time.time()-st)