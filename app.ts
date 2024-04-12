const axios = require('axios');
const readline = require('readline');

// Define the URL of the Flask API endpoint
const apiUrl = 'http://localhost:5000/chatbot';

// Create interface for reading user input from the console
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Function to send a question to the Flask API
function askQuestion(question) {
  axios.post(apiUrl, { question })
    .then(response => {
      console.log('Response:', response.data.response);
      askNextQuestion(); // After receiving response, ask the next question
    })
    .catch(error => {
      console.error('Error:', error.response.data);
      askNextQuestion(); // If error occurs, proceed to next question
    });
}

// Function to ask the next question recursively
function askNextQuestion() {
  rl.question('Enter your question (type "exit" to end): ', (input) => {
    if (input.toLowerCase() === 'exit') {
      rl.close(); // Close the readline interface if 'exit' is entered
    } else {
      askQuestion(input); // Ask the question and wait for response
    }
  });
}

// Start asking the first question
askNextQuestion();

