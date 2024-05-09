from flask import Blueprint, render_template, request, jsonify

module1 = Blueprint('module1', __name__, url_prefix='/module1')

# Define the module structure
module1_structure = {
    'name': 'Module 1: Foundations of Drug Discovery',
    'home_url': 'module1.module1_home',
    'topics': [
        {'name': 'Introduction to the Drug Discovery Pipeline', 'url': 'module1.topic1'},
        {'name': 'Molecular Representation and Similarity Measures', 'url': 'module1.topic2'},
        {'name': 'Exploring Chemical Space and Compound Libraries', 'url': 'module1.topic3'},
        {'name': 'Data Preprocessing and Visualization Techniques', 'url': 'module1.topic4'},
    ],
    'case_study': {'name': 'Case Study: Navigating the Chemical Universe for Hit Identification', 'url': 'module1.case_study'},
    'mini_project': {'name': 'Mini-Project: Building a Molecular Similarity Search Tool', 'url': 'module1.mini_project'}
}

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