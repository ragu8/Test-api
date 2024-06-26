
# Repository Overview

This repository contains the source code for an application built using Python and TypeScript. Below is an overview of the files and instructions to set up and run the repository.

## Files Included

- `app.py`: Python file for the Flask application.
- `app.ts`: TypeScript file for the application.
- `node_modules/`: Directory containing Node.js dependencies.
- `requirements.txt`: File listing Python dependencies.

## Getting Started

Follow the steps below to set up and run the repository on your local machine.

### 1. Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/ragu8/Test-api
```
### 2. Install Python Dependencies

Navigate to the root directory of the project and install the Python dependencies listed in requirements.txt using pip:

```
pip install -r requirements.txt
```
### 3. Install Node.js Dependencies

Navigate to the root directory of the project and install the axios package using npm:

```
npm install axios
```

### 4. Set OpenAI Tokens

Ensure you have your OpenAI tokens set up. Execute the following commands:

```
chmod +x set-tokens.sh
./set-tokens.sh
```

### 5. Running the Applications
Running app.py

To run the app.py file, execute the following command:

```
python3 app.py
```
Create a new window or terminal and navigate to /Test-api. To run the app.ts file, execute the following command:

```
node app.ts
```



