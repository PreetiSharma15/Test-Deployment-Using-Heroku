from flask import Flask
import os
from model_prediction import prediction
app = Flask(__name__)

# freeport =   os.getenv('PORT')
# if(not freeport): freeport = 5000
# print('freeport is: ', freeport)

@app.route("/", methods=['GET'])
def index():
    prediction_class_label = str(prediction())
    return prediction_class_label

# if __name__ == '__main__':
#     app.run(port=freeport, host='localhost')