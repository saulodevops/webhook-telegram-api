# Flask Webhook Telegram API

This project is a Flask application that acts as a webhook for receiving messages from Prometheus and forwarding them to a specified Telegram chat using a bot.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Getting Started](#getting-started)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [Docker](#docker)
- [Contributing](#contributing)
- [License](#license)

## Features

- Receives POST requests from Prometheus.
- Extracts messages from the request body.
- Sends messages to Telegram using a bot.

## Technologies

- Python 3.x
- Flask
- Requests
- Docker (optional)

## Getting Started

To get started with this project, follow the setup instructions below.

## Setup Instructions

1. **Clone the repository**:
```
git clone [https://github.com/yourusername/flask-webhook-to-telegram.git](https://github.com/saulodevops/webhook-telegram-api)
cd webhook-telegram-api
```

2. **Create a virtual environment** (optional but recommended):
```
python -m venv venv
source venv/bin/activate # On Windows use venv\Scripts\activate
```

3. **Install dependencies**:
```
pip install -r requirements.txt
```

4. **Set your environment variables**:
Make sure to set the `CHAT_ID` environment variable with your Telegram chat ID.

## Usage

1. **Run the Flask application**:
```
python app.py
```

2. **Test the webhook**:
You can use tools like Postman or curl to send POST requests to your webhook endpoint (e.g., `http://localhost:5000/webhook`) with a JSON body containing the message.

## Environment Variables

The following environment variable is required:

- `CHAT_ID`: The ID of the Telegram chat where messages will be sent.

You can set this variable in your terminal session or include it in your `.env` file if you are using a package like `python-dotenv`.

## Docker

To run this application in a Docker container:

1. **Build the Docker image**:
```
docker build -t my-flask-app .
```

2. **Run the Docker container**:
```
docker run -d -p 5000:5000 --env CHAT_ID=your_chat_id_here my-flask-app
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

