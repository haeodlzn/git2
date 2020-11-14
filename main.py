from flask import Flask
from config import Config

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/b2')
def branch2():
    return 'Hello, branch2!'

@app.route('/b3')
def branch3():
    return 'Hello, branch3 on github!'

@app.route('/b31')
def branch3():
    return 'Hello, branch31 on local!'

if __name__ == "__main__":
    app.run(host=Config.HOST, port=Config.PORT, debug=Config.PORT)
