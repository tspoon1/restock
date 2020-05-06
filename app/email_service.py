# app/email_service.py

#import key packages/ modules
import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from datetime import datetime

load_dotenv()


#get variables from .env
SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")
SENDGRID_TEMPLATE_ID = os.environ.get("SENDGRID_TEMPLATE_ID")
MY_ADDRESS = os.environ.get("EMAIL")
SUBJECT = 'Restock.io: Updates on the availability and price of your product(s)'

def send_email(customer_name, product, availability):

    now = datetime.now()

    client = SendGridAPIClient(SENDGRID_API_KEY)
    print("CLIENT:", type(client))

    message = Mail(from_email=MY_ADDRESS, to_emails=CUST_ADDRESS, subject=SUBJECT)
    print("MESSAGE:", type(message))

    message.template_id = SENDGRID_TEMPLATE_ID

    message.dynamic_template_data = {
        "name": customer_name,
        "human_friendly_timestamp": now.strftime("%d-%m-%Y %I:%M %p"),
        "product": product,
        "availability": availability
        }

    try:
        response = client.send(message)
        print("RESPONSE:", type(response))
        print(response.status_code)
        print(response.body)
        print(response.headers)

    except Exception as e:
        print("OOPS", e)
