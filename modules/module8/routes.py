from flask import Blueprint, render_template, request, jsonify

module8 = Blueprint('module8', __name__, url_prefix='/module8')

@module8.route('/topic1')
def topic1():
    return render_template('module8/topic1.html')

@module8.route('/topic2')
def topic2():
    return render_template('module8/topic2.html')

@module8.route('/topic3')
def topic3():
    return render_template('module8/topic3.html')

@module8.route('/topic4')
def topic4():
    return render_template('module8/topic4.html')

@module8.route('/topic5')
def topic5():
    return render_template('module8/topic5.html')

@module8.route('/case_study')
def case_study():
    return render_template('module8/case_study.html')

@module8.route('/mini_project')
def mini_project():
    return render_template('module8/mini_project.html')

@module8.route('/')
def module8_home():
    return render_template('module8/module8_home.html')