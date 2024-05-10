from flask import Blueprint, render_template, request, jsonify

module5 = Blueprint('module5', __name__, url_prefix='/module5')

# Define the module structure
module5_structure = {
    'name': 'Module 5: Drug Repurposing and Combination Therapy',
    'home_url': 'module5.module5_home',
    'topics': [
        {'name': 'Network-Based Approaches for Drug Repurposing', 'url': 'module5.topic1'},
        {'name': 'Signature-Based Methods and Transcriptomics in Repurposing', 'url': 'module5.topic2'},
        {'name': 'Identifying Synergistic Drug Combinations', 'url': 'module5.topic3'},
        {'name': 'Clinical and Regulatory Considerations in Drug Repurposing', 'url': 'module5.topic4'},
    ],
    'case_study': {'name': 'Case Study: Repurposing Approved Drugs for Rare Diseases', 'url': 'module5.case_study'},
    'mini_project': {'name': 'Mini-Project: Drug Repurposing using Machine Learning and Network Analysis', 'url': 'module5.mini_project'}
}

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