from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app) 

ollamaUrl = "http://localhost:11434/api/generate" 
modelName = "llama3.2"  

@app.route('/generate', methods=['POST'])
def generate_response():
    try:
        data = request.get_json()
        prompt = data.get("prompt")

        if not prompt:
            return jsonify({"error": "No prompt provided"}), 400

        ollama_payload = {
            "model": modelName,
            "prompt": prompt,
            "stream": False 
        }
        response = requests.post(ollamaUrl, json=ollama_payload)

        if response.status_code == 200:
            response_data = response.json()
            return jsonify({"response": response_data.get("response", "No response received")}), 200
        else:
            return jsonify({"error": "Failed to get response from Ollama"}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)