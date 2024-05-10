from flask import Blueprint, render_template, request, jsonify

module2 = Blueprint('module2', __name__, url_prefix='/module2')

# Define the module structure
module2_structure = {
    'name': 'Module 2: Machine Learning for Drug Property Prediction',
    'home_url': 'module2.module2_home',
    'topics': [
        {'name': 'Regression and Classification Models in Drug Discovery', 'url': 'module2.topic1'},
        {'name': 'Feature Selection and Engineering Techniques', 'url': 'module2.topic2'},
        {'name': 'Model Evaluation, Validation, and Optimization', 'url': 'module2.topic3'},
        {'name': 'Predicting ADME Properties using Machine Learning', 'url': 'module2.topic4'},
    ],
    'case_study': {'name': 'Case Study: Developing a Predictive Model for Drug Solubility', 'url': 'module2.case_study'},
    'mini_project': {'name': 'Mini-Project: QSAR Modeling Challenge for Drug Property Prediction', 'url': 'module2.mini_project'}
}

@module2.route('/topic1')
def topic1():
    return render_template('module2/topic1.html')

@module2.route('/topic2')
def topic2():
    return render_template('module2/topic2.html')

@module2.route('/topic3')
def topic3():
    return render_template('module2/topic3.html')

@module2.route('/topic4')
def topic4():
    return render_template('module2/topic4.html')

@module2.route('/case_study')
def case_study():
    return render_template('module2/case_study.html')

@module2.route('/mini_project')
def mini_project():
    return render_template('module2/mini_project.html')

@module2.route('/')
def module2_home():
    return render_template('module2/module2_home.html')