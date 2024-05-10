from flask import Blueprint, render_template, request, jsonify

module4 = Blueprint('module4', __name__, url_prefix='/module4')

@module4.route('/topic1')
def topic1():
    return render_template('module4/topic1.html')

@module4.route('/topic2')
def topic2():
    return render_template('module4/topic2.html')

@module4.route('/topic3')
def topic3():
    return render_template('module4/topic3.html')

@module4.route('/topic4')
def topic4():
    return render_template('module4/topic4.html')

@module4.route('/topic5')
def topic5():
    return render_template('module4/topic5.html')

@module4.route('/topic6')
def topic6():
    return render_template('module4/topic6.html')

@module4.route('/case_study')
def case_study():
    return render_template('module4/case_study.html')

@module4.route('/mini_project')
def mini_project():
    return render_template('module4/mini_project.html')

@module4.route('/')
def module4_home():
    return render_template('module4/module4_home.html')