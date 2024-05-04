from flask import Blueprint, request, jsonify
from collections import deque

api = Blueprint('api', __name__, url_prefix='/api')
responses = deque()  # This will store the generated responses

def llm_generate(prompt, context):
    # Placeholder for the LLM generation logic
    return "Generated response for: " + prompt

@api.route('/generate', methods=['POST'])
def generate():
    prompt = request.form['prompt']
    context = request.form['context']
    
    generated_content = llm_generate(prompt, context)
    responses.append(generated_content)  # Store the generated content
    
    return jsonify({'generated_content': generated_content})

@api.route('/delete', methods=['POST'])
def delete():
    # Deletes the oldest generated content
    if responses:
        responses.popleft()
    return jsonify({'status': 'success', 'message': 'Oldest content deleted'})
