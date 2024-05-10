from flask import Blueprint, render_template, request, jsonify

module3 = Blueprint('module3', __name__, url_prefix='/module3')

@module3.route('/topic1')
def topic1():
    return render_template('module3/topic1.html')

@module3.route('/topic2')
def topic2():
    return render_template('module3/topic2.html')

@module3.route('/topic3')
def topic3():
    return render_template('module3/topic3.html')

@module3.route('/topic4')
def topic4():
    return render_template('module3/topic4.html')

@module3.route('/topic5')
def topic5():
    return render_template('module3/topic5.html')

@module3.route('/topic6')
def topic6():
    return render_template('module3/topic6.html')

@module3.route('/case_study')
def case_study():
    return render_template('module3/case_study.html')

@module3.route('/mini_project')
def mini_project():
    return render_template('module3/mini_project.html')

@module3.route('/')
def module3_home():
    return render_template('module3/module3_home.html')