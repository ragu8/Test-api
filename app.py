from flask import Flask, request, jsonify
from dotenv import load_dotenv
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain_community.chat_models import ChatOpenAI

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Initialize Chat model
chat = ChatOpenAI(temperature=0.5)

# Initialize flow messages
flow_messages = []

# Define initial system messages
initial_messages = [
    SystemMessage(content="You are a Travel AI assistant."),
    SystemMessage(content="Rather than travel questions, you reply (I am a Travel AI assistant only please ask on that)."),
    SystemMessage(content="I'm here to assist you with your travel plans. Please provide the following information:"),
    SystemMessage(content="question 1. Number of people traveling with you."),
    SystemMessage(content="question 2. Destination(s) of your travel."),
    SystemMessage(content="question 3. Date(s) of your travel."),
    SystemMessage(content="question 4. Type of travel (e.g., business, family, personal)."),
    SystemMessage(content="question 5. Preferences for your travel destination (e.g., beach, mountains, historical cities)."),
    SystemMessage(content="Please make sure to provide all the requested information to receive a tailored travel plan."),
    SystemMessage(content="If any information is missing and all information important, I will ask you for clarification one by one."),
    SystemMessage(content="ask question one by one "),
    SystemMessage(content="Let's get started!")
]

flow_messages += initial_messages

# Function to get response from the Chat model
def get_chatmodel_response(question):
    flow_messages.append(HumanMessage(content=question))
    answer = chat(flow_messages)
    flow_messages.append(AIMessage(content=answer.content))
    return answer.content

# API endpoint for chatbot interaction
@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.json
    input_question = data.get('question', '')

    if not input_question.strip():
        return jsonify({'response': 'Please provide a question.'}), 400

    response = get_chatmodel_response(input_question)
    return jsonify({'response': response}), 200

if __name__ == '__main__':
    app.run(debug=True)


# curl -X POST http://localhost:5000/chatbot -H "Content-Type: application/json" -d '{"question": "How many people are traveling with me?"}'




