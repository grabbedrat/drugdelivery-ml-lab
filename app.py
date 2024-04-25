from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/module1')
def module1():
    return render_template('module1/module1.html')

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

if __name__ == '__main__':
    app.run(debug=True)