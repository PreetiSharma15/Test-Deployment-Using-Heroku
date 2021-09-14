from flask import Flask
import os

app = Flask(__name__)

# freeport =   os.getenv('PORT')
# if(not freeport): freeport = 5000
# print('freeport is: ', freeport)

@app.route("/", methods=['GET'])
def index():
    return "Hello World!"

# if __name__ == '__main__':
#     app.run(port=freeport, host='localhost')