# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import subprocess

# app = Flask(__name__)
# CORS(app)

# @app.route('/explain', methods=['POST'])
# def explain():
#     data = request.get_json()
#     text = data.get("text", "")
#     prompt = f"Explain this phrase in simple terms: \"{text}\""

#     # Use Ollama CLI to query Mistral locally
#     result = subprocess.run(
#         ['ollama', 'run', 'mistral', prompt],
#         stdout=subprocess.PIPE,
#         text=True
#     )

#     explanation = result.stdout.strip()
#     return jsonify({"explanation": explanation})

# if __name__ == '__main__':
#     app.run(debug=True, port=5050)

from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__,static_folder='front',static_url_path='/')
CORS(app)

@app.route('/')
def index():
    return app.send_static_file('index.html')
@app.route('/explain', methods=['POST'])
def explain():
    data = request.get_json()
    text = data.get("text", "")
    prompt = f"Explain this phrase in simple terms: \"{text}\""

    # Use Ollama CLI to query MiniCPM locally
    result = subprocess.run(
        ['ollama', 'run', 'minicpm-v:latest', prompt],
        stdout=subprocess.PIPE,
        text=True
    )

    explanation = result.stdout.strip()
    return jsonify({"explanation": explanation})

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    text = data.get("text", "")
    prompt = f"Answer as an intelligent assistant: {text}"  # <-- updated line

    result = subprocess.run(
        ['ollama', 'run', 'minicpm-v', prompt],  # your current model
        stdout=subprocess.PIPE,
        text=True
    )

    explanation = result.stdout.strip()
    return jsonify({"explanation": explanation})

if __name__ == '__main__':
    app.run(debug=True, port=5050)
