from flask import Flask, render_template,jsonify
import pandas as pd

import sys

sys.path.append("../nfl_project/static/python_scripts/")

from model_run_v1 import runme
# create instance of Flask app
app = Flask(__name__)


# create route that renders index.html template
@app.route("/")
def echo():
    return render_template("index.html")

@app.route("/x") 
def prediction():
    #runs the model
    print("/x")
    pre=runme()
    return jsonify(pre)

#@app.route("/y") 
#def teams():
#    #creates list of team name
#    df = pd.read_csv('nfl_project/static/resources/Teams.csv')
#    return df.to_json(orient='records')








if __name__ == "__main__":
    app.run(debug=True)
