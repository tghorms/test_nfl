from flask import Flask, render_template,jsonify
import pandas as pd
import tensorflow as tf
import keras
import sys
import numpy as np

#from model_run_v1 import suckit
from static.python_scripts.model_run_v1 import runme,load_models
# create instance of Flask app
app = Flask(__name__)

# create route that renders index.html template
@app.route("/")
def echo():
    return render_template("index.html")
@app.route('/x/<TeamH>/<TeamA>/<BookScore>')

def prediction(TeamH,TeamA,BookScore):
    model = load_models()

    XDF=pd.read_csv('../nfl_project/static/resources/2019-Team-Metrics-Final.csv')
    print(XDF)
    print(TeamH)
    #team_select = XDF.loc[TeamH]
    #print(team_select)
    #home_team = XDF['Team'].unique()
    #print(home_team)


    
    return jsonify({'x':'x'})

@app.route("/y") 
def teams():
    #creates list of team name
    df = pd.read_csv('./static/resources/Teams.csv')
    return df.to_json(orient='records')


if __name__ == "__main__":
 
   app.run(debug=True)
   