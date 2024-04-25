from flask import Flask, render_template, request, jsonify
import requests
import pandas as pd
from io import StringIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/module1')
def module1():
    return render_template('module1/module1.html')

@app.route('/data-exploration')
def data_exploration():
    return render_template('data_exploration.html')

@app.route('/module1/introduction')
def module1_introduction():
    return render_template('module1/introduction.html')

@app.route('/module1/theoretical-background')
def module1_theoretical_background():
    return render_template('module1/theoretical_background.html')

@app.route('/module1/data-exploration')
def module1_data_exploration():
    return render_template('module1/data_exploration.html')

@app.route('/module1/feature-engineering')
def module1_feature_engineering():
    return render_template('module1/feature_engineering.html')

@app.route('/module1/model-building')
def module1_model_building():
    return render_template('module1/model_building.html')

@app.route('/module1/model-evaluation')
def module1_model_evaluation():
    return render_template('module1/model_evaluation.html')

@app.route('/module1/model-interpretation')
def module1_model_interpretation():
    return render_template('module1/model_interpretation.html')

@app.route('/module1/demo')
def module1_demo():
    return render_template('module1/demo.html')

@app.route('/module1/exercises-quizzes')
def module1_exercises_quizzes():
    return render_template('module1/exercises_quizzes.html')

@app.route('/module1/discussion-reflection')
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
            'num_samples': len(dataset),
            'num_features': len(dataset.columns) - 1,
            # Add more dataset information and analysis results
        }
        
        print('Dataset loaded successfully!')
        return jsonify(dataset_info)
    except Exception as e:
        error_message = f"Error loading dataset: {str(e)}"
        print(error_message)
        return jsonify({'error': error_message}), 400

if __name__ == '__main__':
    app.run(debug=True)