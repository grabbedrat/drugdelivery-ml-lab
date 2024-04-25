from flask import Flask, render_template, request, jsonify, Blueprint
import requests
import pandas as pd
import random 
import numpy as np
from io import StringIO

app = Flask(__name__)

# Create a blueprint for the module1 routes
module1_bp = Blueprint('module1', __name__, url_prefix='/module1')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data-exploration')
def data_exploration():
    return render_template('data_exploration.html')

@module1_bp.route('/')
def module1():
    return render_template('module1/module1.html')

@module1_bp.route('/introduction')
def module1_introduction():
    return render_template('module1/introduction.html')

@module1_bp.route('/theoretical-background')
def module1_theoretical_background():
    return render_template('module1/theoretical_background.html')

@module1_bp.route('/data-exploration')
def module1_data_exploration():
    return render_template('module1/data_exploration.html')

@module1_bp.route('/feature-engineering')
def module1_feature_engineering():
    return render_template('module1/feature_engineering.html')

@module1_bp.route('/model-building')
def module1_model_building():
    return render_template('module1/model_building.html')

@module1_bp.route('/model-evaluation')
def module1_model_evaluation():
    return render_template('module1/model_evaluation.html')

@module1_bp.route('/model-interpretation')
def module1_model_interpretation():
    return render_template('module1/model_interpretation.html')

@module1_bp.route('/demo')
def module1_demo():
    return render_template('module1/demo.html')

@module1_bp.route('/exercises-quizzes')
def module1_exercises_quizzes():
    return render_template('module1/exercises_quizzes.html')

@module1_bp.route('/discussion-reflection')
def module1_discussion_reflection():
    return render_template('module1/discussion_reflection.html')

@app.route('/api/datasets', methods=['POST'])
def load_dataset():
    dataset_url = request.json['url']
    print(f'Loading dataset from: {dataset_url}')

    try:
        # Download the dataset content using requests with SSL certificate verification disabled
        response = requests.get(dataset_url, verify=False)
        response.raise_for_status()  # Raise an exception for unsuccessful status codes

        # Load the dataset from the downloaded content
        dataset = pd.read_csv(StringIO(response.text))
        print(f'Dataset shape: {dataset.shape}')

        # Perform dataset processing and analysis
        dataset_info = {
            'name': 'Delaney Dataset',
            'description': 'Solubility data for a diverse set of compounds.',
            'num_samples': int(len(dataset)),
            'num_features': int(len(dataset.columns) - 1),
            'features': dataset.columns[:-1].tolist(),
            'target': dataset.columns[-1],
            'sample_data': dataset.head(5).to_dict(orient='records'),
            'summary': {},
            'histogram': {},
            'boxplot': {},
            'scatterplot': {},
            'feature_importance': {},
            'related_modules': [
                {'name': 'Data Preprocessing', 'url': '/module2'},
                {'name': 'Feature Selection', 'url': '/module3'},
                {'name': 'Model Training', 'url': '/module4'},
            ],
        }

        # Perform summary statistics for each feature
        for column in dataset.columns[:-1]:
            summary = dataset[column].describe().to_dict()
            dataset_info['summary'][column] = {
                'description': f'Summary statistics for {column}',
                'data_type': str(dataset[column].dtype),
                'missing_values': int(dataset[column].isnull().sum()),
                'stats': {k: v.item() if isinstance(v, np.generic) else v for k, v in summary.items()},
            }

        # Generate histogram data for the target variable
        target_feature = dataset.columns[-1]
        dataset_info['histogram'] = {
            'data': dataset[target_feature].tolist(),
            'xaxis': target_feature,
        }

        # Generate boxplot data for a selected feature
        boxplot_feature = dataset.columns[1]  # Example: Use the second feature for boxplot
        dataset_info['boxplot'] = {
            'data': dataset[boxplot_feature].tolist(),
            'yaxis': boxplot_feature,
        }

        # Generate scatterplot data for two selected features
        scatter_feature_x = dataset.columns[0]  # Example: Use the first feature for x-axis
        scatter_feature_y = dataset.columns[1]  # Example: Use the second feature for y-axis
        dataset_info['scatterplot'] = {
            'x': dataset[scatter_feature_x].tolist(),
            'y': dataset[scatter_feature_y].tolist(),
            'xaxis': scatter_feature_x,
            'yaxis': scatter_feature_y,
        }

        # Generate feature importance data (example: random values)
        dataset_info['feature_importance'] = {
            'features': dataset.columns[:-1].tolist(),
            'importance': [random.random() for _ in range(len(dataset.columns) - 1)],
        }

        print('Dataset loaded successfully!')
        return jsonify(dataset_info)

    except Exception as e:
        error_message = f"Error loading dataset: {str(e)}"
        print(error_message)
        return jsonify({'error': error_message}), 400

# Register the module1 blueprint
app.register_blueprint(module1_bp)

if __name__ == '__main__':
    app.run(debug=True)