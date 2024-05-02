from flask import Blueprint, render_template

module3 = Blueprint('module3', __name__, url_prefix='/module3')

@module3.route('/lesson1')
def lesson1():
    return render_template('module3/lesson1.html')

@module3.route('/lesson2')
def lesson2():
    return render_template('module3/lesson2.html')

@module3.route('/lesson3')
def lesson3():
    return render_template('module3/lesson3.html')

@module3.route('/case_study')
def case_study():
    return render_template('module3/case_study.html')
