from flask import request, Flask # requires flask! please download before running :)
from flask import render_template
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()
name = os.getenv("NAME")
email = os.getenv("EMAIL")

@app.route('/api/getpi')
def getpi():
    if request.method == 'GET':
        try:
            f = open("picalc/pi.txt", "r")
            return f.read()
        except:
            return "picalc/pi.txt wasn't found! Contact " + name + " at " + email + " if this persists."
    else:
        return "Invaild method! /getpi is designed for GET requests, not " + request.method
    
@app.route('/api/postpi', methods=['POST', 'GET'])
def postpi():
    if request.form['pi']:
        if request.form['pi'].startswith("3.14") == True:
            with open("picalc/pi.txt", "w") as f:
                f.write(request.form['pi'])
        else:
            return "Invalid string!"

@app.route('/')
def lander():
    try:
        f = open("picalc/pi.txt", "r")
        piresult = f.read()
        if piresult == "No clients have connected yet. Become one of the first!":
            piresult = "No clients have connected. Become one of the first!"
        else:
            piresult = "Current Pi count is " + piresult
    except:
        piresult = "picalc/pi.txt wasn't found on this web server. Sorry!"
    if request.method == 'GET':
            return render_template('index.html', pi=piresult, name=name, email=email)
    else:
        return "Please use GET to access this page."