from PIL import Image;
import pytesseract as pt
import cv2
import numpy as np
import re
from fuzzywuzzy import fuzz,process
from copy import deepcopy

#%% Global Variables

errorList = ['FileNotFoundError','AssertionError', 'AttributeError', 'EOFError', 'FloatingPointError', 'GeneratorExit', 'ImportError', 'IndexError', 'KeyError', 'KeyboardInterrupt', 'MemoryError', 'NameError', 'NotImplementedError', 'OSError', 'OverflowError', 'ReferenceError', 'RuntimeError', 'StopIteration', 'SyntaxError', 'IndentationError', 'TabError', 'SystemError', 'SystemExit', 'TypeError', 'UnboundLocalError', 'UnicodeError', 'UnicodeEncodeError', 'UnicodeDecodeError', 'UnicodeTranslateError', 'ValueError', 'ZeroDivisionError']
tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'

#%% iMAGE tO eRROR fUNCTIONS


def imageToText(img):
    im_gray = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    thresh = cv2.threshold(im_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    text = pt.image_to_string(thresh,config=tessdata_dir_config,lang="eng")
    return text



#%% Error Processing

def ret_formattedList(text):
    textList = text.split('\n')
    formattedList=[]
    
    for el in textList:
        if ""!=el and re.match(" +",el) is None:
            formattedList.append(el)
            
    return formattedList
            
        

def findError(formattedList):
    for a in formattedList[-3:]:
        if re.search("[Et].r+.",a):
            errorMsg = a.split(" ")[0]
        
    if errorMsg is not None:
        print(process.extract(errorMsg,errorList,scorer=fuzz.token_set_ratio)[0][0])
    else:
        print("Bad Screenshot")


def findErrorLine(formattedList):
    tempList = deepcopy(formattedList)
    tempList.reverse()
    for a in tempList[:5]:
        if re.search("File",a) is not None and re.search("line ",a) is not None:
            errorLine = a.split(',')[1].split(" ")[2]
            break
        
    if errorLine is not None:
        print("Error line is ",errorLine)    
    else:
        print("Bad Screenshot")
        


#%% tHE fUNCTIONAL cOMMANDS
        

def errorAPI(img):
    formattedList = ret_formattedList(imageToText(img))
    findError(formattedList)
    findErrorLine(formattedList)



#%%


# img=cv2.imread(r"D:\Ram\Internship\Virtual Doubt Assistant\Take 2\img.png",0).astype(np.uint8)
# ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)


# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
# opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
# invert = 255 - opening


# (thresh, im_bw) = cv2.threshold(im_gray, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# filtered=cv2.adaptiveThreshold(im_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,31,1)

    



