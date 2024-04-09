const axios = require('axios');

// Define the URL of the Flask API endpoint
const apiUrl = 'http://localhost:5000/chatbot';

// Define the question to ask
const question = 'How many people are traveling with me?';

// Make a POST request to the Flask API
axios.post(apiUrl, { question })
  .then(response => {
    console.log('Response:', response.data.response);
  })
  .catch(error => {
    console.error('Error:', error.response.data);
  });
