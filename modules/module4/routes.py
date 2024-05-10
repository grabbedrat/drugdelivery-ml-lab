from flask import Blueprint, render_template, request, jsonify

module4 = Blueprint('module4', __name__, url_prefix='/module4')

# Define the module structure
module4_structure = {
    'name': 'Module 4: Ligand-Based Drug Design',
    'home_url': 'module4.module4_home',
    'topics': [
        {'name': 'Pharmacophore Modeling and its Applications', 'url': 'module4.topic1'},
        {'name': 'Quantitative Structure-Activity Relationship (QSAR) Modeling', 'url': 'module4.topic2'},
        {'name': 'Similarity Searching and Clustering in Ligand-Based Design', 'url': 'module4.topic3'},
        {'name': 'Integration of Ligand and Structure-Based Approaches', 'url': 'module4.topic4'},
    ],
    'case_study': {'name': 'Case Study: Designing Potent and Selective GPCR Ligands', 'url': 'module4.case_study'},
    'mini_project': {'name': 'Mini-Project: Ligand-Based Virtual Screening and Optimization', 'url': 'module4.mini_project'}
}

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

@module4.route('/case_study')
def case_study():
    return render_template('module4/case_study.html')

@module4.route('/mini_project')
def mini_project():
    return render_template('module4/mini_project.html')

@module4.route('/')
def module4_home():
    return render_template('module4/module4_home.html')