from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Existing chat endpoint
@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_query = data.get('message')

        chatbot_response = generate_chatbot_response(user_query)

        return jsonify({'response': chatbot_response})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)}), 500

def generate_chatbot_response(user_query):
    if "hello" in user_query.lower():
        return "Hello there! How can I help you?"
    elif "goodbye" in user_query.lower():
        return "Goodbye! Have a great day."
    else:
        return f"I received your message: {user_query}. I'm a simple bot, but I'll try my best."

# New inference endpoint
@app.route('/infer', methods=['POST'])
def infer():
    try:
        data = request.get_json()
        text = data.get('text')  # Expecting a 'text' field in the JSON payload

        if not text:
            return jsonify({'error': 'No text provided'}), 400

        # Simple rule-based sentiment inference
        prediction = simple_sentiment_inference(text)

        return jsonify({
            'text': text,
            'prediction': prediction
        })

    except Exception as e:
        print(f"Error in inference: {e}")
        return jsonify({'error': str(e)}), 500

def simple_sentiment_inference(text):
    """
    A basic rule-based sentiment analysis inference.
    Returns 'positive', 'negative', or 'neutral' based on simple keyword matching.
    """
    text = text.lower()
    positive_words = ['good', 'great', 'happy', 'awesome', 'love']
    negative_words = ['bad', 'terrible', 'sad', 'hate', 'awful']

    positive_count = sum(1 for word in positive_words if word in text)
    negative_count = sum(1 for word in negative_words if word in text)

    if positive_count > negative_count:
        return 'positive'
    elif negative_count > positive_count:
        return 'negative'
    else:
        return 'neutral'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=False)
