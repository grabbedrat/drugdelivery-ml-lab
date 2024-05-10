from flask import Blueprint, render_template, request, jsonify

module7 = Blueprint('module7', __name__, url_prefix='/module7')

# Define the module structure
module7_structure = {
    'name': 'Module 7: Cheminformatics Tools and Techniques',
    'home_url': 'module7.module7_home',
    'topics': [
        {'name': 'Molecular Descriptors and Fingerprints', 'url': 'module7.topic1'},
        {'name': 'Similarity Searching and Clustering Techniques', 'url': 'module7.topic2'},
        {'name': 'Managing and Querying Chemical Databases', 'url': 'module7.topic3'},
        {'name': 'Cheminformatics Workflows and Automation', 'url': 'module7.topic4'},
    ],
    'case_study': {'name': 'Case Study: Integrating Cheminformatics in Drug Discovery Projects', 'url': 'module7.case_study'},
    'mini_project': {'name': 'Mini-Project: Building a Cheminformatics Pipeline for Virtual Screening', 'url': 'module7.mini_project'}
}

@module7.route('/topic1')
def topic1():
    return render_template('module7/topic1.html')

@module7.route('/topic2')
def topic2():
    return render_template('module7/topic2.html')

@module7.route('/topic3')
def topic3():
    return render_template('module7/topic3.html')

@module7.route('/topic4')
def topic4():
    return render_template('module7/topic4.html')

@module7.route('/case_study')
def case_study():
    return render_template('module7/case_study.html')

@module7.route('/mini_project')
def mini_project():
    return render_template('module7/mini_project.html')

@module7.route('/')
def module7_home():
    return render_template('module7/module7_home.html')