from flask import Flask, request
import requests
import os

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook_handler():
    # Extract data from Prometheus request
    incoming_data = request.get_json()
    print("Received data:", incoming_data)  # For debugging
    text = incoming_data.get('message')  # Adjust this based on your JSON structure
    
    chat_id = os.getenv('CHAT_ID')  # This retrieves the chat_id from the environment variable

    send_message_to_telegram(chat_id, text)

    # Return acknowledgment
    return {'status': 'Message received'}, 200

def send_message_to_telegram(chat_id, text):
    token = 'your_bot_token_here'  # Replace with your bot token
    url = f'https://api.telegram.org/bot{token}/sendMessage'

    payload = {
        'chat_id': chat_id,
        'text': text,
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        print("Message sent successfully.")
    else:
        print("Failed to send message:", response.json())

# Check the response status code
if response.status_code == 200:
    print("Success:", response.json())  # Print the JSON response if successful
else:
    print("Error:", response.status_code)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
