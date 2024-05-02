from flask import Blueprint, render_template

module5 = Blueprint('module5', __name__, url_prefix='/module5')

@module5.route('/lesson1')
def lesson1():
    return render_template('module5/lesson1.html')

@module5.route('/lesson2')
def lesson2():
    return render_template('module5/lesson2.html')

@module5.route('/lesson3')
def lesson3():
    return render_template('module5/lesson3.html')

@module5.route('/case_study')
def case_study():
    return render_template('module5/case_study.html')
