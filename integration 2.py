from flask import Flask,render_template,request
import vidToAud as v
import newTrial as nt
import ocr as o
import search2 as s

#%% gLOBAL vARIABLES

app = Flask(__name__)


#%% vARIOUS fUNCTIONALITY


def uploadVideo(videoName):
    text = v.vidToAud(videoName,videoName)
    keys = v.theProcessing(videoName,text)
    keys["problem_name"] = keys["problem_name"].split('.')[0]
    nt.enterInMongoDB(keys)


def searchOCR(img):
    o.errorAPI(img)

def searchVideo():
    pass

@app.route('/',methods=["GET","POST"])
def homePage():
    return render_template("index.html")


@app.route('/index',methods=["GET","POST"])
def thisIs():
    return render_template("index.html")

@app.route('/search',methods=["GET","POST"])
def searchPage():
    print("in search")
    return render_template("search.html")

@app.route('/searchResult',methods=["GET","POST"])
def searchResult():
    data = request.form['searchBox']
    li=s.searchInElasticSearch(data)
    if len(li)>0:
        return render_template("searchResult.html",data=li)
    else:
        return render_template("searchResult.html",data="Nothing to show")

@app.route('/upload',methods=["GET","POST"])
def uploadPage():
    return render_template("upload.html")

@app.route('/ocr',methods=["GET","POST"])
def ocrPage():
    return render_template("ocr.html")
    
if __name__=="__main__":
    app.run(host="0.0.0.0", port=1020)