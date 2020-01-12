# load and evaluate a saved model
from tensorflow.keras.models import load_model
import numpy as np
import os
import pandas as pd
def load_models():
    mymodel=None
    # modelfile=os.path.dirname(__file__) +'\\vince-model-final.h5'
    modelfile = 'vince-model-final.h5'
    # print('modelisat'+modelfile)    
    mymodel = load_model(modelfile)
    return mymodel

def runme(model,TeamH,TeamA,BT):   
    vdf= pd.read_csv('.//static//resources//2019-Team-Metrics-Final.csv')

    #creating an ndarry to pass to the model-- home & away
    #ha2p = np.array([[0.275,-0.127,41.77,3.08,0.089,0.051,0.038,6.83,0.794,0.367,0.177,0.253,0.127,2.07,5.45,0.672,6.96,30.37,1.67,0.149,0.081,0.068,5.89,0.673,0.168,0.168,0.398,0.193,1,4.73,0.477,9.39,0.227,-0.034,39.07,2.7,0.083,0.032,0.051,6.44,0.761,0.295,0.218,0.308,0.135,1.35,4.84,0.54,4.6,34.84,1.85,0.135,0.098,0.037,6.55,0.729,0.215,0.129,0.356,0.16,1.67,4.28,0.509,6.67]])
    ha1p=vdf['Team']== TeamH
    print(ha1p)
    #ha2p=vdf['Team']== TeamA
    #ha3p=pd.concat('ha1p','ha2p')
    #print(ha1p)
    #david=ha3p.to_numpy()
    print(vdf)
    #print(david)
    #ha2p=vdf.query(Team==TeamA)
    bookTotal=BT
    ##total prediction
    xaway = ''
    #yaway = model.predict(xaway)
    #myindex = 0
    #print(f"X={xaway[myindex]}, Predicted={yaway[myindex]}")

    #Pscore = int(yaway[myindex])

    ##logic for over under
    x = ''
    if Pscore > bookTotal:
        x = 'Over'
    elif Pscore < bookTotal:
        x = 'Under'
    else:
        x = 'Even'
    return x
