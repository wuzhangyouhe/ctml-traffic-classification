#from __future__ import unicode_literals
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
import logging
from django.http import JsonResponse
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import pylab as pl
import pandas as pd
from csv import reader
from sklearn import datasets, linear_model, neighbors
import os
import warnings
from sklearn.model_selection import train_test_split
# Load libraries
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.externals.six import StringIO  
from IPython.display import Image  
from sklearn.tree import export_graphviz
from sklearn.externals import joblib 
import subprocess
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.mime.application import MIMEApplication


warnings.filterwarnings(action="ignore", module="scipy", message="^internal gelsd")

logger = logging.getLogger(__name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def index(request):
    return render(request, "index.html")

def from_string(s):
  "Convert dotted IPv4 address to integer."
  return reduce(lambda a,b: a<<8 | b, map(int, s.split(".")))

def to_string(ip):
  "Convert 32-bit integer to dotted IPv4 address."
  return ".".join(map(lambda n: str(ip>>n & 0xFF), [24,16,8,0]))

# Load a CSV file
def load_csv(filename):
    file = open(filename, "rU")
    lines = reader(file)
    dataset = list(lines)
    return dataset

def getFileData(request):

    if request.method == 'GET':

        filePath = request.GET.get('path')
        print "filePath = " + filePath

        fullFilePath = BASE_DIR + filePath
        fileContent = load_csv(fullFilePath)
        # print fileContent

        partialContent = fileContent[0:5]

        response = JsonResponse(partialContent, safe=False)

        return HttpResponse(response, status=200)


def train(request):

    if request.method == 'GET':

        return HttpResponse("GET /train", status=200)

    elif request.method == 'POST':

        # user input parameters
        dataX = request.POST.get('data_x_url','')
        dataY = request.POST.get('target_y_url','')

        dataXFullPath = BASE_DIR + dataX
        dataYFullPath = BASE_DIR + dataY

        #get dataset
        dataset = pandas.read_csv(dataYFullPath)

        # split dataset
        array = dataset.values
        X = array[:,0:61]
        Y = array[:,61]
        validation_size = 0.30
        seed = 42
        X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)

        # apply to CART algorithm
        rfc = RandomForestClassifier()
        rfc.fit(X_train, Y_train)
        filename = 'finalized_model.sav'
        joblib.dump(rfc, filename)
        # load the model from disk
        loaded_model = joblib.load(filename)
        result = loaded_model.score(X_validation, Y_validation)
        
        # response with the result
        response = JsonResponse(result, safe=False)
        return response


def predict(request):

    if request.method == 'GET':

        return HttpResponse("GET /predict", status=200)

    elif request.method == 'POST':

        # Real data collecting for traffic application classification" 
        subprocess.call(["sh", "cdata.sh"])
        subprocess.call(["sleep", "2"])

        #data collection finished with Tshark, wait 5 second for data cleaning"
        file1 = pd.read_csv("predict_apply.csv")
        file1.shape
        file1.isnull().sum

        # step-1 to replace all empty/null to be empty
        update_file = file1.fillna(" ")
        update_file.isnull().sum()
        update_file.to_csv('update_'+"predict_apply.csv", index = False)
        
        # step-2 to remove all rows with empty value
        update_file = file1.fillna(0)
        update_file['tcp.flags'] = update_file['tcp.flags'].apply(lambda  x: int(str(x), 16))
        update_file['ip.src']=update_file['ip.src'].apply(lambda x: from_string(x))
        update_file['ip.dst']=update_file['ip.dst'].apply(lambda x: from_string(x))
        update_file.to_csv('update_'+"predict_apply.csv", index = False)
        subprocess.call(["sudo", "tcpflow", "-a", "-o", "predict", "-r", "predict.pcap"])
        loaded_model = joblib.load('finalized_model.sav')

        # Compute predict result with features
        predict_file = pandas.read_csv('update_predict_apply.csv')
        predict_label = loaded_model.predict(predict_file)

        frequency = {}
        for word in predict_label:
            count = frequency.get(word,0)
            frequency[word] = count + 1
     
        frequency_list = frequency.keys()
 
        for key, value in sorted(frequency.iteritems(), key=lambda (k,v): (v,k), reverse=True):
            print "%s: %s" % (key, value)

        print("Pickup the most freqent packet in the flow: ")
        mostFreq = ''
        mostFreqCount = 0
        for k in frequency:
           if frequency[k] > mostFreqCount:
             mostFreqCount = frequency[k]
             mostFreq = k
        print (mostFreq)

        # response with the result
        result = mostFreq
        response = JsonResponse(result, safe=False)
        
	    # sent an email
        msg = MIMEMultipart()
        msg['Subject'] = "Test notification! Alter action"
        body = "Alert Notfication from ML tool for classificating the network traffic. \n Dear, are you accessing " + mostFreq + " website ?"
        msg.attach(MIMEText(body, 'plain'))

        # the attachment
        part = MIMEApplication(open('predict/report.pdf', 'rb').read())
        part.add_header('Content-Disposition', 'attachment', filename='report.pdf')
        msg.attach(part)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("IW2018networking@gmail.com", "IW2018net")
        server.sendmail("IW2018networking@gmail.com", "e0146965@u.nus.edu", msg.as_string())
        print('e-mail sent!')
        server.quit()
 
        return response
