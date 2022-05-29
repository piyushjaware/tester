from crypt import methods
from re import A
from urllib import request
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/report", methods=['GET', 'POST'])
def report():
    return render_template('report.html')


@app.route("/success")
def success():
    return render_template('success.html')