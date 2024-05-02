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

# Module 1 routes
@app.route('/modules/module1/lesson1')
def module1_lesson1():
    return render_template('modules/module1/lesson1.html')

@app.route('/modules/module1/lesson2')
def module1_lesson2():
    return render_template('modules/module1/lesson2.html')

@app.route('/modules/module1/lesson3')
def module1_lesson3():
    return render_template('modules/module1/lesson3.html')

# Module 2 routes
@app.route('/modules/module2/lesson1')
def module2_lesson1():
    return render_template('modules/module2/lesson1.html')

@app.route('/modules/module2/lesson2')
def module2_lesson2():
    return render_template('modules/module2/lesson2.html')

@app.route('/modules/module2/lesson3')
def module2_lesson3():
    return render_template('modules/module2/lesson3.html')

@app.route('/modules/module2/project')
def module2_project():
    return render_template('modules/module2/project.html')

# Module 3 routes
@app.route('/modules/module3/lesson1')
def module3_lesson1():
    return render_template('modules/module3/lesson1.html')

@app.route('/modules/module3/lesson2')
def module3_lesson2():
    return render_template('modules/module3/lesson2.html')

@app.route('/modules/module3/lesson3')
def module3_lesson3():
    return render_template('modules/module3/lesson3.html')

@app.route('/modules/module3/case-study')
def module3_case_study():
    return render_template('modules/module3/case_study.html')

# Module 4 routes
@app.route('/modules/module4/lesson1')
def module4_lesson1():
    return render_template('modules/module4/lesson1.html')

@app.route('/modules/module4/lesson2')
def module4_lesson2():
    return render_template('modules/module4/lesson2.html')

@app.route('/modules/module4/lesson3')
def module4_lesson3():
    return render_template('modules/module4/lesson3.html')

@app.route('/modules/module4/project')
def module4_project():
    return render_template('modules/module4/project.html')

# Module 5 routes
@app.route('/modules/module5/lesson1')
def module5_lesson1():
    return render_template('modules/module5/lesson1.html')

@app.route('/modules/module5/lesson2')
def module5_lesson2():
    return render_template('modules/module5/lesson2.html')

@app.route('/modules/module5/lesson3')
def module5_lesson3():
    return render_template('modules/module5/lesson3.html')

@app.route('/modules/module5/case-study')
def module5_case_study():
    return render_template('modules/module5/case_study.html')

@app.route('/notebooks/<path:filename>')
def serve_notebook(filename):
    return send_from_directory('static/notebooks', filename)

if __name__ == '__main__':
    app.run(debug=True)
