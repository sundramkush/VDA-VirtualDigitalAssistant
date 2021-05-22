#%% Library Imports

import subprocess
import time
import speech_recognition as sr
import re
import string
import nltk
import json
import time
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from fuzzywuzzy import fuzz,process


#%% Global Variables

start = time.time()
r = sr.Recognizer()
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))
d={}
videosContent=[]
# Command for converting video to audio



#%% Video Processing Functions


def audToText(fileName):
    f1 = open("f1.txt","w+")
    with sr.AudioFile("D:\Ram\Internship\Virtual Doubt Assistant\Take 2\VidWaves\{}".format(fileName.split(".")[0]+'.wav')) as source:
        audio_text = r.listen(source)
        try:
            text = r.recognize_google(audio_text).lower()
            # f1.write(text)
            # f1.close()
        except:
            text = "shakalaka boom boom"
            # f1.write("nthng nthng nthng")
            
        finally:
            return text
            # f1.close()


def vidToAud(fileName,audioname):
    cmd = 'ffmpeg -y -i "{}" \
        -ab 160k -ac 2 -ar 44100 -vn "D:\Ram\Internship\Virtual Doubt Assistant\Take 2\VidWaves\{}.wav"'.format(fileName,audioname.split('.')[0])
    subprocess.call(cmd,shell=True)
    text = audToText(audioname)
    return text

#%% Natural Language Processing

def theProcessing(name,text):
    
    d,vidContent={},{}
    keywords=[]
    
    # f1 = open("f1.txt", "r")
    # f2 = open("vidList.json","a+")
    # text = f1.read()
    #Removing all numbers
    noNum = re.sub(r'\d+','',text)
    
    #Removing all punctuations
    noPunc = noNum.translate(str.maketrans("","", string.punctuation))
    
    #Removing stopwords
    tokens = word_tokenize(noPunc)
    noStops = [i for i in tokens if not i in stop_words]
    
    #Stemming each word
    noInflections = []
    for word in noStops:
        noInflections.append(lemmatizer.lemmatize(word))
            
    
    for word in noInflections:
        if word in d:
            d[word]+=1
        else:
            d[word]=1
            
    max_freq = max(d.values())
    
    for word in d.keys():
        d[word]=d[word]/max_freq
        if d[word]>0.333 : keywords.append(word)
        
    
    
    vidContent["problem_name"] = name
    vidContent["keywords"] = keywords
    
    return vidContent
    # print(vidContent)
            
    # f2.write(json.dumps(vidContent))
    # f2.close()
    # f1.close()
    
    
    


#%% The Search

searchResult ={}

for content in videosContent:
    print(process.extract("layout",content["keywords"],limit=1,scorer=fuzz.token_set_ratio),"\n\n")
    print(content["id"])




    