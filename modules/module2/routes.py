from flask import Blueprint, render_template

module2 = Blueprint('module2', __name__, url_prefix='/module2')

@module2.route('/lesson1')
def lesson1():
    return render_template('module2/lesson1.html')

@module2.route('/lesson2')
def lesson2():
    return render_template('module2/lesson2.html')

@module2.route('/lesson3')
def lesson3():
    return render_template('module2/lesson3.html')

@module2.route('/project')
def project():
    return render_template('module2/project.html')
