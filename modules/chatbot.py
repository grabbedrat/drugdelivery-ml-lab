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
        return f'<p><strong>Student:</strong> {prompt} </p><p><strong>LLM:</strong> {response}</p>'
    except Exception as e:
        return str(e), 400

generate_response = lambda prompt, context: "I'm sorry, I don't have a response for that."
