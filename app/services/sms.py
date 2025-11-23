from twilio.rest import Client
import os

async def send_sms(to: str, body: str):
    sid = os.getenv('TWILIO_ACCOUNT_SID')
    token = os.getenv('TWILIO_AUTH_TOKEN')
    from_number = os.getenv('TWILIO_PHONE_NUMBER')
    if not sid or not token:
        print(f'Mock SMS to {to}: {body}')
        return
    client = Client(sid, token)
    client.messages.create(body=body, from_=from_number, to=to)
