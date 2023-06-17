import os
from flask import Flask, request

from twilio.twiml.messaging_response import MessaginResponse, Message
from twilio.rest import Client

TWILIO_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
app = Flask(__name__)

@app.route('/send-sms', methods=['POST'])
def send_sms():
    response = MessagingResponse()
    response.message('Testing sending a SMS!')
    from_number = request.form['From']
    to_number = request.form['To']
    client.messages.create(body='This is an SMS to send!', from_=from_number, to=to_number)

@app.route('/')
def home():
    return 'Hello World!'
