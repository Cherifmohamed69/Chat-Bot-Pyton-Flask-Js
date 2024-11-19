from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load questions and responses
with open('questions.json', 'r') as f:
    qa_data = json.load(f)

@app.route('/')
def index():
    return render_template('index.html', questions=qa_data)

@app.route('/get-response', methods=['POST'])
def get_response():
    data = request.json
    selected_question = data.get('question')
    # Find the response for the selected question
    response = next((qa['response'] for qa in qa_data if qa['question'] == selected_question), "I don't know the answer to that.")
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
