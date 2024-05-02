from flask import Flask, render_template, request, jsonify, Blueprint, send_from_directory
import requests
import pandas as pd
import random
import numpy as np
from io import StringIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data-exploration')
def data_exploration():
    return render_template('data_exploration.html')

@app.route('/modules/module1')
def module1():
    return render_template('modules/module1.html')

@app.route('/modules/module2')
def module2():
    return render_template('modules/module2.html')

@app.route('/notebooks/<path:filename>')
def serve_notebook(filename):
    return send_from_directory('static/notebooks', filename)

# Add the remaining routes and functionality

if __name__ == '__main__':
    app.run(debug=True)
