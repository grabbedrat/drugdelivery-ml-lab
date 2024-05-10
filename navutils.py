from flask import current_app

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

module6_structure = {
    'name': 'Module 6: Toxicity Prediction and Risk Assessment',
    'home_url': 'module6.module6_home',
    'topics': [
        {'name': 'Mechanisms of Drug Toxicity and Adverse Events', 'url': 'module6.topic1'},
        {'name': 'QSAR Models for Toxicity Prediction', 'url': 'module6.topic2'},
        {'name': 'Mining and Analysis of Adverse Event Databases', 'url': 'module6.topic3'},
        {'name': 'Integrating Toxicity Prediction in Drug Development', 'url': 'module6.topic4'},
    ],
    'case_study': {'name': 'Case Study: Assessing the Cardiac Toxicity Risk of Drug Candidates', 'url': 'module6.case_study'},
    'mini_project': {'name': 'Mini-Project: Building a Multi-Endpoint Toxicity Prediction Model', 'url': 'module6.mini_project'}
}

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

def register_context_processors(app):
    @app.context_processor
    def inject_modules():
        """
        Context processor to make the module structures available to all templates.
        """
        module_structures = [
            module1_structure,
            module2_structure,
            module3_structure,
            module4_structure,
            module5_structure,
            module6_structure,
            module7_structure


        ]
        return dict(modules=module_structures)