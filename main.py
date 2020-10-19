from flask import Flask, render_template, request
import flask
from werkzeug.datastructures import ImmutableMultiDict

app = Flask(__name__)
app.secret_key = 'lol'

@app.route('/home', methods=["POST","GET"])
def main():
    return "Some text"

@app.route('/', methods=["POST","GET"])
def home():
    if request.method == "GET":
        return render_template('index.html')
    elif request.method == "POST":
        pass

if __name__ == '__main__':
    app.run(debug=True)