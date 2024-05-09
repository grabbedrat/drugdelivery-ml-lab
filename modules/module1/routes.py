from flask import Blueprint, render_template, request, jsonify

module1 = Blueprint('module1', __name__, url_prefix='/module1')

@module1.route('/topic1')
def topic1():
   return render_template('module1/topic1.html')

@module1.route('/topic2')
def topic2():
   return render_template('module1/topic2.html')

@module1.route('/topic3')
def topic3():
   return render_template('module1/topic3.html')

@module1.route('/topic4')
def topic4():
   return render_template('module1/topic4.html')

@module1.route('/case_study')
def case_study():
   return render_template('module1/case_study.html')

@module1.route('/mini_project')
def mini_project():
   return render_template('module1/mini_project.html')

@module1.route('/')
def module1_home():
   return render_template('module1/module1_home.html')