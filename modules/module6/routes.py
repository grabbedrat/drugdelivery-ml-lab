from flask import Blueprint, render_template, request, jsonify

module6 = Blueprint('module6', __name__, url_prefix='/module6')

@module6.route('/topic1')
def topic1():
    return render_template('module6/topic1.html')

@module6.route('/topic2')
def topic2():
    return render_template('module6/topic2.html')

@module6.route('/topic3')
def topic3():
    return render_template('module6/topic3.html')

@module6.route('/topic4')
def topic4():
    return render_template('module6/topic4.html')

@module6.route('/case_study')
def case_study():
    return render_template('module6/case_study.html')

@module6.route('/mini_project')
def mini_project():
    return render_template('module6/mini_project.html')

@module6.route('/')
def module6_home():
    return render_template('module6/module6_home.html')