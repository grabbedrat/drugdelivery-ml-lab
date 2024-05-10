from flask import Blueprint, render_template, request, jsonify

module5 = Blueprint('module5', __name__, url_prefix='/module5')

@module5.route('/topic1')
def topic1():
    return render_template('module5/topic1.html')

@module5.route('/topic2')
def topic2():
    return render_template('module5/topic2.html')

@module5.route('/topic3')
def topic3():
    return render_template('module5/topic3.html')

@module5.route('/topic4')
def topic4():
    return render_template('module5/topic4.html')

@module5.route('/case_study')
def case_study():
    return render_template('module5/case_study.html')

@module5.route('/mini_project')
def mini_project():
    return render_template('module5/mini_project.html')

@module5.route('/')
def module5_home():
    return render_template('module5/module5_home.html')