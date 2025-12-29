from twilio.rest import Client
import os

def send_whatsapp(message: str, to_number: str):
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    from_number = os.getenv("TWILIO_WHATSAPP_FROM")

    client = Client(account_sid, auth_token)

    msg = client.messages.create(
        from_=f"whatsapp:{from_number}",
        body=message,
        to=f"whatsapp:{to_number}"
    )

    return msg.sid
