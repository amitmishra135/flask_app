from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/hello_world1")
def hello_world1():
    return "<h1>Hello, World!1</h1>"

@app.route("/test")
def test():
    a=10+20
    return "this is my print function {}".format(a)

@app.route("/test2/test2")
def test2():
    #for taking argument at the client side import request library
    data = request.args.get('x')
    return "this is my print function {}".format(data)


@app.route("/hello_world2")
def hello_world2():
    return "<h1>Hello, World!2</h1>" 
if __name__=="__main__":
    app.run(host="0.0.0.0")
