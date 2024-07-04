import mlflow
# An object of Flask class is our WSGI application.
from flask import Flask, request
import pickle
import numpy as np
import pandas as pd
import json

import sys
sys.path.append('/workspaces/mlops_zoomcamp_project/')

from utils.preprocessing import *

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

uri = '/workspaces/mlops_zoomcamp_project/02-experiment-tracking/mlruns/2/e6b8b8c4e9864995ac5be24d398a6ec4/artifacts/model'
model = mlflow.pyfunc.load_model(uri)


# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.

# Route to check if Flask is running
@app.route('/')
def index():
    return "Flask is running!"


@app.route('/api', methods=['POST'])
def serve():
    
    data = request.get_json(force=True)
    features = prepare_features(data)
    prediction = model.predict(features)

    return json.dumps(prediction[0], default=int)

# main driver function
if __name__ == '__main__':
    app.run(port=5000, debug=True)