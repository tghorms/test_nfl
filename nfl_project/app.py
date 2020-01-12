from flask import Flask, render_template,jsonify
import pandas as pd
import tensorflow as tf
import keras
import sys
import numpy as np
import csv
from numpy import loadtxt

#from model_run_v1 import suckit
# from static.python_scripts.model_run_v1 import runme,load_models
from static.python_scripts.model_run_v1 import load_models
# create instance of Flask app
app = Flask(__name__)

@app.before_first_request
def dataload():
    global football
  

# create route that renders index.html template
@app.route("/")
def echo():
    return render_template("index.html")
@app.route('/x/<TeamH>/<TeamA>/<BookScore>')

def prediction(TeamH,TeamA,BookScore):


    # XDF=pd.read_csv('./static/resources/2019-Team-Metrics-Final.csv')

    # for each line in XDF:
    #     print(line)


    stats = np.empty
    with open('./static/resources/2019-Team-Metrics-Final.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if row [0] == TeamH:
                for x in row[1:]:
                    stats = np.append(stats, x)
                
                # print(row)

    with open('./static/resources/2019-Team-Metrics-Final.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if row [0] == TeamA:
                test = row[1:]
                for x in test :
                    stats = np.append(stats, x)
        # print(stats)
    
    npx = stats[1:65]

    # x = dataset[:,0]
    
    # x = dataset.reshape((0,64))
    #print(team_select)
    #home_team = XDF['Team'].unique()
    #print(home_team)
    football = load_models()
    graph = tf.get_default_graph()
    with graph.as_default():
        prediction = football.predict([[npx]])
    result = {'x':int(prediction[0][0])}
    print(result)
    return jsonify(result)

@app.route("/y") 
def teams():
    #creates list of team name
    df = pd.read_csv('./static/resources/Teams.csv')
    return df.to_json(orient='records')


if __name__ == "__main__":
 
   app.run(debug=True)
   