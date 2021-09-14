from flask import Flask
import os
from model_prediction import prediction
app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    prediction_class_label = str(prediction())
    return prediction_class_label
