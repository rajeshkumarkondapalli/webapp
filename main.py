#!/bin/bash

# Create the directory structure
mkdir -p chatbot_app/backend

# Create backend files
cat > chatbot_app/backend/app.py <<EOL
from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_query = data.get('message')

        # Generate response without database storage
        chatbot_response = generate_chatbot_response(user_query)

        return jsonify({'response': chatbot_response})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)}), 500

def generate_chatbot_response(user_query):
    """
    Simple chatbot logic without database
    """
    if "hello" in user_query.lower():
        return "Hello there! How can I help you?"
    elif "goodbye" in user_query.lower():
        return "Goodbye! Have a great day."
    else:
        return f"I received your message: {user_query}. I'm a simple bot, but I'll try my best."

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=False)
