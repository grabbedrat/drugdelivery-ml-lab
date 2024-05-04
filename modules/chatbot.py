from flask import Blueprint, request, jsonify, render_template

chatbot_bp = Blueprint('chatbot', __name__)

messages = []

@chatbot_bp.route('/chatbot', methods=['POST'])
def chatbot():
    try:
        prompt = request.form['prompt']
        context = request.form['context']

        # Generate response using the prompt and context
        response = generate_response(prompt, context)

        message_id = len(messages)
        messages.append({'id': message_id, 'role': 'user', 'content': prompt})
        messages.append({'id': message_id + 1, 'role': 'assistant', 'content': response})

        # Return the last message as HTML
        return f'<p><strong>Student:</strong> {prompt} </p><p><strong>Assistant:</strong> {response}</p>'
    except Exception as e:
        return str(e), 400

@chatbot_bp.route('/chatbot/<int:message_id>', methods=['DELETE'])
def delete_message(message_id):
    messages[:] = [m for m in messages if m['id'] != message_id]
    return '', 204

def generate_response(prompt, context):
    # Placeholder function for generating responses
    return f"Generated response for: {prompt}"
