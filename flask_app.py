from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")  # Ensure to set this in your environment

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']

    # Create a response using the OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use the appropriate model
        messages=[{"role": "user", "content": user_message}]
    )

    bot_reply = response['choices'][0]['message']['content']
    return jsonify({'response': bot_reply})

if __name__ == '__main__':
    app.run(debug=True)
