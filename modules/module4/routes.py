from flask import Blueprint, render_template

module4 = Blueprint('module4', __name__, url_prefix='/module4')

@module4.route('/lesson1')
def lesson1():
    return render_template('module4/lesson1.html')

@module4.route('/lesson2')
def lesson2():
    return render_template('module4/lesson2.html')

@module4.route('/lesson3')
def lesson3():
    return render_template('module4/lesson3.html')

@module4.route('/project')
def project():
    return render_template('module4/project.html')
