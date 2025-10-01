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
    f = open("picalc/pi.txt", "r")
    if request.form['pi']:
        if f.read() == "No clients have connected yet. Become one of the first!":
            if request.form['pi'].startswith("3.14") == True:
                with open("picalc/pi.txt", "w") as f:
                    f.write(request.form['pi'])
            else:
                return "Invalid string!"
        else:
            if request.form['pi'].startswith(f.read()) == True:
                with open("picalc/pi.txt", "w") as f:
                    f.write(request.form['pi'])
            else:
                return "Invalid string!"
    else:
        return "Request not found!"

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
        ver = open("ver.txt", "r")
        version = ver.read()
        return render_template('index.html', pi=piresult, name=name, email=email, version=version)
    else:
        return "Please use GET to access this page."

@app.route('/api/getver')
def getver():
    try:
        f = open("ver.txt", "r")
        version = f.read()
        return version
    except:
        return "ver.txt not found on server"
    
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404