# load and evaluate a saved model
from numpy import loadtxt
from keras.models import load_model
import numpy as np
import os

def runme():
    # load model

    file_name = os.path.dirname(__file__) +'/model_home.h5'
    print(file_name)
    model = load_model(os.path.dirname(__file__) +'/model_home.h5')
    
    #poll the average data for the two teams.
    
    #todo
    
    #creating an ndarry to pass to the model-- home & away
    ha2p = np.array([[12,15,2019,27,4,2,0,0,0,37,2019,4.8,5.2,0.16,0.091,0.297,0.309,4.7,4.9,0.198,0.124,0.282,0.235,18.6,20.5,18.3,16.4,0.339,0.364,38,42,0.342,0.595,0.358,0.359,43,40,0.512,0.575]])

    aa2p = np.array([[12,15,2019,27,4,17,0,0,0,37,2019,4.8,5.2,0.16,0.091,0.297,0.309,4.7,4.9,0.198,0.124,0.282,0.235,18.6,20.5,18.3,16.4,0.339,0.364,38,42,0.342,0.595,0.358,0.359,43,40,0.512,0.575]])

    #vegas total to compare against
    bookTotal = 40

    #home prediction
    xhome = ha2p
    yhome = model.predict(xhome)
    myindex = 0
    #print(f"X={xhome[myindex]}, Predicted={yhome[myindex]}")

    #away prediction
    xaway = aa2p
    yaway = model.predict(xaway)
    myindex = 0
    #print(f"X={xaway[myindex]}, Predicted={yaway[myindex]}")

    homescore = int(yhome[myindex])
    awayscore = int(yaway[myindex])
    predicted_score = homescore + awayscore

    #logic for over under
    x = ''
    if predicted_score > bookTotal:
        x = 'Over'
    elif predicted_score > bookTotal:
        x = 'Under'
    else:
        x = 'Even'
    
    print(x)
    return x
