from flask import current_app

# Define the module structure
module1_structure = {
    'name': 'Module 1: Foundations of Drug Discovery',
    'home_url': 'module1.module1_home',
    'topics': [
        {'name': 'Introduction to the Drug Discovery Pipeline', 'url': 'module1.topic1'},
        {'name': 'Molecular Representation, Similarity, and Chemical Space Exploration', 'url': 'module1.topic2'},  # Merged topics
        {'name': 'Data Preprocessing and Visualization Techniques', 'url': 'module1.topic3'},
        {'name': 'Data Integration and Multi-Modal Analysis', 'url': 'module1.topic4'},
        {'name': 'Data Quality and Curation in Drug Discovery', 'url': 'module1.topic5'},  # Added topic
    ],
    'case_study': {'name': 'Case Study: Navigating the Chemical Universe for Hit Identification', 'url': 'module1.case_study'},
    'mini_project': {'name': 'Mini-Project: Building a Molecular Similarity Search Tool', 'url': 'module1.mini_project'}
}

module2_structure = {
    'name': 'Module 2: Cheminformatics Tools and Techniques',  # Reordered module
    'home_url': 'module2.module2_home',
    'topics': [
        {'name': 'Molecular Descriptors and Fingerprints', 'url': 'module2.topic1'},
        {'name': 'Similarity Searching and Clustering Techniques', 'url': 'module2.topic2'},
        {'name': 'Managing and Querying Chemical Databases', 'url': 'module2.topic3'},
        {'name': 'Cheminformatics Workflows and Automation', 'url': 'module2.topic4'},
        {'name': 'Handling Big Data in Cheminformatics', 'url': 'module2.topic5'},
    ],
    'case_study': {'name': 'Case Study: Integrating Cheminformatics in Drug Discovery Projects', 'url': 'module2.case_study'},
    'mini_project': {'name': 'Mini-Project: Building a Cheminformatics Pipeline for Virtual Screening', 'url': 'module2.mini_project'}
}

module3_structure = {
    'name': 'Module 3: Machine Learning for Drug Property Prediction',
    'home_url': 'module3.module3_home',
    'topics': [
        {'name': 'Regression and Classification Models in Drug Discovery', 'url': 'module3.topic1'},
        {'name': 'Feature Selection and Engineering Techniques', 'url': 'module3.topic2'},
        {'name': 'Model Evaluation, Validation, and Optimization', 'url': 'module3.topic3'},
        {'name': 'Predicting ADME Properties using Machine Learning', 'url': 'module3.topic4'},
        {'name': 'Deep Learning for Drug Property Prediction', 'url': 'module3.topic5'},
        {'name': 'Model Interpretation and Explainability in Drug Property Prediction', 'url': 'module3.topic6'},  # Added topic
    ],
    'case_study': {'name': 'Case Study: Developing a Predictive Model for Drug Solubility', 'url': 'module3.case_study'},
    'mini_project': {'name': 'Mini-Project: QSAR Modeling Challenge for Drug Property Prediction', 'url': 'module3.mini_project'}
}

module4_structure = {
    'name': 'Module 4: Structure-Based Drug Design',
    'home_url': 'module4.module4_home',
    'topics': [
        {'name': 'Understanding Protein-Ligand Interactions', 'url': 'module4.topic1'},
        {'name': 'Molecular Docking: Principles and Applications', 'url': 'module4.topic2'},
        {'name': 'Virtual Screening Strategies for Lead Identification', 'url': 'module4.topic3'},
        {'name': 'Structure-Based Lead Optimization Techniques', 'url': 'module4.topic4'},
        {'name': 'Protein-Protein Interactions and Allosteric Targeting', 'url': 'module4.topic5'},
        {'name': 'Molecular Dynamics Simulations for Understanding Protein-Ligand Interactions', 'url': 'module4.topic6'},  # Added topic
    ],
    'case_study': {'name': 'Case Study: Designing Selective Kinase Inhibitors', 'url': 'module4.case_study'},
    'mini_project': {'name': 'Mini-Project: Virtual Screening Campaign for a Novel Drug Target', 'url': 'module4.mini_project'}
}

module5_structure = {
    'name': 'Module 5: Ligand-Based Drug Design',
    'home_url': 'module5.module5_home',
    'topics': [
        {'name': 'Pharmacophore Modeling and its Applications', 'url': 'module5.topic1'},
        {'name': 'Quantitative Structure-Activity Relationship (QSAR) Modeling', 'url': 'module5.topic2'},
        {'name': 'Similarity Searching and Clustering in Ligand-Based Design', 'url': 'module5.topic3'},
        {'name': 'Integration of Ligand and Structure-Based Approaches', 'url': 'module5.topic4'},
        {'name': 'De Novo Drug Design using Generative Models', 'url': 'module5.topic5'},
        {'name': 'Multi-Objective Optimization in Ligand-Based Drug Design', 'url': 'module5.topic6'},  # Added topic
    ],
    'case_study': {'name': 'Case Study: Designing Potent and Selective GPCR Ligands', 'url': 'module5.case_study'},
    'mini_project': {'name': 'Mini-Project: Ligand-Based Virtual Screening and Optimization', 'url': 'module5.mini_project'}
}

module6_structure = {
    'name': 'Module 6: Drug Safety and Repurposing',
    'home_url': 'module6.module6_home',
    'topics': [
        {'name': 'Network-Based Approaches for Drug Repurposing', 'url': 'module6.topic1'},
        {'name': 'Signature-Based Methods and Transcriptomics in Repurposing', 'url': 'module6.topic2'},
        {'name': 'Identifying Synergistic Drug Combinations', 'url': 'module6.topic3'},
        {'name': 'Mechanisms of Drug Toxicity and Adverse Events', 'url': 'module6.topic4'},
        {'name': 'QSAR Models for Toxicity Prediction', 'url': 'module6.topic5'},
        {'name': 'Mining and Analysis of Adverse Event Databases', 'url': 'module6.topic6'},
        {'name': 'Integrating Toxicity Prediction in Drug Development', 'url': 'module6.topic7'},
    ],
    'case_study': {'name': 'Case Study: Repurposing Approved Drugs for Rare Diseases', 'url': 'module6.case_study'},
    'mini_project': {'name': 'Mini-Project: Drug Repurposing using Machine Learning and Network Analysis', 'url': 'module6.mini_project'}
}

module7_structure = {
    'name': 'Module 7: Translational Informatics and Precision Medicine',
    'home_url': 'module7.module7_home',
    'topics': [
        {'name': 'Introduction to Translational Informatics', 'url': 'module7.topic1'},
        {'name': 'Biomarker Discovery and Validation', 'url': 'module7.topic2'},
        {'name': 'Omics Data Integration and Analysis', 'url': 'module7.topic3'},
        {'name': 'Personalized Medicine and Pharmacogenomics', 'url': 'module7.topic4'},
        {'name': 'Clinical Trial Design and Informatics', 'url': 'module7.topic5'},  # Added topic
    ],
    'case_study': {'name': 'Case Study: Implementing Precision Medicine in Oncology', 'url': 'module7.case_study'},
    'mini_project': {'name': 'Mini-Project: Developing a Precision Medicine Strategy for a Complex Disease', 'url': 'module7.mini_project'}
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