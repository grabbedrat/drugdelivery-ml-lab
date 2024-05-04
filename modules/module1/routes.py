from flask import Blueprint, render_template, request, jsonify

module1 = Blueprint('module1', __name__, url_prefix='/module1')

@module1.route('/lesson1')
def lesson1():
    return render_template('module1/lesson1.html')

@module1.route('/lesson2')
def lesson2():
    return render_template('module1/lesson2.html')

@module1.route('/lesson3')
def lesson3():
    return render_template('module1/lesson3.html')

@module1.route('/')
def module1_home():
    return render_template('module1/module1_home.html')
