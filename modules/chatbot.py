# chatbot.py
from flask import Blueprint, request, jsonify, render_template

chatbot_bp = Blueprint('chatbot', __name__)

messages = []

@chatbot_bp.route('/chatbot', methods=['POST'])
def chatbot():
    try:
        prompt = request.form['prompt']

        # Generate response using the prompt and context
        response = generate_response(prompt)

        message_id = len(messages)
        messages.append({'id': message_id, 'role': 'user', 'content': prompt})
        messages.append({'id': message_id + 1, 'role': 'assistant', 'content': response})

        # Return the last two messages as HTML
        return '\n'.join(f'<p>{message["role"]}: {message["content"]}</p>' for message in messages[-2:])
    except Exception as e:
        return str(e), 400

@chatbot_bp.route('/chatbot/<int:message_id>', methods=['DELETE'])
def delete_message(message_id):
    messages[:] = [m for m in messages if m['id'] != message_id]
    return '', 204

def generate_response(prompt):
    # Placeholder function for generating responses
    return f"Generated response for: {prompt}"
