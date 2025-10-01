from flask import request, Flask # requires flask! please download before running :)
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
    
@app.route('/api/postpi')
def postpi():
    if request.method == 'POST':
        return "Not Implemented"
    else:
        return "Invalid method! /postpi is designed for POST requests, not " + request.method

@app.route('/')
def lander():
    if request.method == 'GET':
        return "Not implemented"
    else:
        return "Please use GET to access this page."