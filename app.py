#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Main Server File for running the flask app.
@Title: app.py
@Author: Mphatso
"""

# Import Third Party Modules

import os
from flask import Flask, request, render_template
from flask_cors import CORS
import requests
  
apiToken = "ea547439ae2aad787c4c84bc8d32a4e13d423ff2"


# Support for gomix's 'front-end' and 'back-end' UI.
app = Flask(__name__, static_folder='public', template_folder='views')

# Enable CORS
CORS(app)

# Set the app secret key from the secret environment variables.
app.secret = os.environ.get('SECRET')

# Setup Flask functions and end routes
@app.route('/')
def homepage():
    """
    Displays the homepage.
    
    Returns: 
        render template for index.html
    """
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Simple Route to get authorization from LabGuru using user credentials

    Returns:
        String: Authorization Token 
    """
    email = request.args['email']
    password = request.args['password']

    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'login': email, 'password': password}

    # defining a URL to call
    URL = "https://my.labguru.com/api/v1/sessions"

    # sending get request and saving the response as response object
    r = requests.post(url = URL, params = PARAMS)
    
    # extracting data in json format
    data = r.json()
    # print(data)
    return data

@app.route('/loadBox', methods=['GET', 'POST'])
def loadBox():
    """Simple Route to gather consumables from a LabGuru Box

    Returns:
        JSON: Box Data
    """
    token = request.args['token']
    boxId = request.args['boxId']

    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'token': token}

    # defining a URL to call
    URL = "https://my.labguru.com/api/v1/boxes/" + boxId

    # sending get request and saving the response as response object
    r = requests.get(url = URL, params = PARAMS)
    
    # extracting data in json format
    data = r.json()
    # print(data)
    return data

@app.route('/read', methods=['GET', 'POST'])
def read():
    """
    Simple endpoint to fetch the stock and read and jsonify it to be used in javascript
    Returns: 
        Data of chosen item
    """

    stockID = "806"  

    if 'id' in request.args:
        stockID = request.args['id']
        print(stockID)

    # print(request.args['id'])

    URL = "https://my.labguru.com/api/v1/stocks/" + stockID

    # location given here
    apiToken = "ea547439ae2aad787c4c84bc8d32a4e13d423ff2"
    
    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'token':apiToken}

    # sending get request and saving the response as response object
    r = requests.get(url = URL, params = PARAMS)
    
    # extracting data in json format
    data = r.json()

    return data

@app.route('/write', methods=['GET','POST','PUT'])
def write():
    """
    Simple endpoint to edit the chosen stock and change it's amount
    Returns: 
        Submitted data
    """

    stockID = "866"  

    if 'id' in request.args:
        stockID = request.args['id']
        print(stockID)

    amount = request.args['amount']

    # print(request.args['id'])

    URL = "https://my.labguru.com/api/v1/stocks/" + stockID

    # location given here
    
    # defining a params dict for the parameters to be sent to the API
    DATA = {'token':apiToken,'item':{'weight':amount} }

    # sending get request and saving the response as response object
    r = requests.put(url = URL, json = DATA)
    
    # extracting data in json format
    data = r.json()

    return data

if __name__ == '__main__':
    app.run()