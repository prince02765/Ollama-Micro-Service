# Ollama Microservice

This project is a microservice built using **Flask** and **Python** to interact with a locally installed **Ollama LLM**. The service provides an API to send queries to the **Ollama** model via the command line.

---

##  Tech Stack

- **Ollama** (Locally installed LLM)
- **Python** (Backend development)
- **Flask** (Microservice framework)
- **REST API** (For communication)

---

# Installation & Setup for Windows

## Install [Ollama Locally](https://ollama.com/download/OllamaSetup.exe), [Python](https://www.python.org/downloads/), [VS Code](https://code.visualstudio.com/download), [Postman](https://www.postman.com/downloads/)

## Clone This Repository

```bash

git clone https://github.com/prince02765/Ollama-Micro-Service
cd ollama-microservice
python -m venv venv
venv\Scripts\activate
pip install flask requests flask-cors
python3 app.py
```

# Testing the API in Postman

## Create a New POST Request

Select POST as the request type.

Enter Following URL:
```bash
http://localhost:5000/generate
```

## Set Request Headers

Add the following key-value pair:

```bash
Content-Type : application/json
```

## Provide Request Body

Select raw and choose JSON

Enter the following JSON payload:
```bash

{
  "prompt": "What is Ollama?"
}

```

## Send the Request

Sample Response:
```bash

{
  "response": "ChatGPT is a computer program that uses natural language processing (NLP) to generate human-like text responses. It's a large language model developed by the company OpenAI, which is designed to simulate conversation with users.\n\nChatGPT is capable of understanding and responding to user input in a way that seems natural and context-specific. It can be used for a variety of purposes, such as:\n\n1. Customer service: ChatGPT can be used to provide customer support and answer frequently asked questions.\n2. Language translation: ChatGPT can translate text from one language to another.\n3. Writing assistance: ChatGPT can assist with writing tasks, such as suggesting alternative phrases or ideas.\n4. Content creation: ChatGPT can generate content, such as articles, social media posts, and even entire books.\n\nChatGPT uses a technique called transformer architecture to process and generate text. This architecture allows the model to learn patterns in language and generate text that is coherent and context-specific.\n\nSome of the key features of ChatGPT include:\n\n1. Contextual understanding: ChatGPT can understand the context of a conversation and respond accordingly.\n2. Natural language generation: ChatGPT can generate text that sounds natural and conversational.\n3. Adaptability: ChatGPT can adapt to different topics and domains, making it useful for a wide range of applications.\n\nOverall, ChatGPT is an advanced language model that can simulate human-like conversation and provide valuable assistance in various areas."
}

```


![image_2025-02-04_18-25-12](https://github.com/user-attachments/assets/a5115968-8c79-41d6-9a37-077db8e78bb4)










