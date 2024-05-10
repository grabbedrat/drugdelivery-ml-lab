from flask import Blueprint, render_template, request, jsonify

module3 = Blueprint('module3', __name__, url_prefix='/module3')

# Define the module structure
module3_structure = {
    'name': 'Module 3: Structure-Based Drug Design',
    'home_url': 'module3.module3_home',
    'topics': [
        {'name': 'Understanding Protein-Ligand Interactions', 'url': 'module3.topic1'},
        {'name': 'Molecular Docking: Principles and Applications', 'url': 'module3.topic2'},
        {'name': 'Virtual Screening Strategies for Lead Identification', 'url': 'module3.topic3'},
        {'name': 'Structure-Based Lead Optimization Techniques', 'url': 'module3.topic4'},
    ],
    'case_study': {'name': 'Case Study: Designing Selective Kinase Inhibitors', 'url': 'module3.case_study'},
    'mini_project': {'name': 'Mini-Project: Virtual Screening Campaign for a Novel Drug Target', 'url': 'module3.mini_project'}
}

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

@module3.route('/case_study')
def case_study():
    return render_template('module3/case_study.html')

@module3.route('/mini_project')
def mini_project():
    return render_template('module3/mini_project.html')

@module3.route('/')
def module3_home():
    return render_template('module3/module3_home.html')