from flask import Blueprint, request, jsonify, render_template
from openai import OpenAI
import os
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key='sk-proj-wFfDKarW3XQQNbzbb6ihT3BlbkFJZfPM0ShQlxehp7eIX6Ld')

chatbot_bp = Blueprint('chatbot', __name__)

messages = []

@chatbot_bp.route('/chatbot', methods=['POST'])
def chatbot():
    try:
        exercise_number = None
        for field_name in request.form:
            if field_name.startswith('prompt_'):
                exercise_number = field_name.split('_')[1]
                break

        if exercise_number:
            prompt = request.form[f'prompt_{exercise_number}']
            context = request.form[f'context_{exercise_number}']

            # Generate response using the prompt and context
            response = generate_response(prompt, context)

            message_id = len(messages)
            messages.append({'id': message_id, 'role': 'user', 'content': prompt})
            messages.append({'id': message_id + 1, 'role': 'assistant', 'content': response})

            # Return the last message as HTML
            return f'<p><strong>Student:</strong> {prompt} </p><p><strong>gpt-3.5-turbo-instruct:</strong> {response}</p>'
        else:
            return "Invalid request", 400

    except Exception as e:
        return str(e), 400

def generate_response(prompt, context):
    # Combine the context and prompt for the LLM input
    input_text = f"{context}\nStudent: {prompt}\nLLM:"
    
    # Make the API request to OpenAI
    response = client.completions.create(model='gpt-3.5-turbo-instruct',  # Choose an appropriate language model
    prompt=input_text,
    max_tokens=100,  # Adjust the response length as needed
    )
    
    # Extract the generated response from the API response
    generated_response = response.choices[0].text.strip()
    
    return generated_response