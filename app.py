from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app) 

ollamaUrl = "http://localhost:11434/api/generate" # Ollama API URL for local server
modelName = "llama3.2" # Ollama Model name

@app.route('/generate', methods=['POST']) # POST method to generate response from Ollama
def generate_response():
    try: # Try block to handle exceptions
        data = request.get_json()
        prompt = data.get("prompt")

        if not prompt: # Check if prompt is provided
            return jsonify({"error": "No prompt provided"}), 400

        ollama_payload = { # Payload to send to Ollama API
            "model": modelName,
            "prompt": prompt,
            "stream": False 
        }
        response = requests.post(ollamaUrl, json=ollama_payload) # POST request to Ollama API

        if response.status_code == 200: # Check if response is successful
            response_data = response.json()
            return jsonify({"response": response_data.get("response", "No response received")}), 200
        else: # Return error if response is not successful
            return jsonify({"error": "Failed to get response from Ollama"}), 500

    except Exception as e: # Return error if exception occurs
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000) # Run the Flask app on port 5000