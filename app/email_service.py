# app/email_service.py

#import key packages/ modules
import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from datetime import datetime


def send_email(customer_name, customer_address, product, availability):

    load_dotenv()
    
    #get variables from .env
    SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")
    MY_ADDRESS = os.environ.get("EMAIL")

    now = datetime.now()
    date_and_time = now.strftime("%d-%m-%Y %I:%M %p")
    CUST_ADDRESS = customer_address
    SUBJECT = 'Restock.io: Updates on the availability and price of your product(s)'


    client = SendGridAPIClient(SENDGRID_API_KEY)
    print("CLIENT:", type(client))

    html = f"""

    <img src="https://media1.s-nbcnews.com/j/newscms/2018_29/2473831/180622-amazon-mc-1124_36a8ba8a051fde1141e943390ac804f9.fit-760w.JPG">

    <h4>Dear {customer_name},</h4>
    <p>Date: {date_and_time}</p>


    <p>We hope this email finds you well. You are receiving this notification as part of your product monitoring subscription with Restock.io.</p>

    <p>Below, we have listed the product you wanted to watch</p>

    <p> {product} is currently {availability}
    <p>Thank you for trusting us as your shopping helper! Please give us a shout by sharing this service with your friends/ family: we are here to help.</p>


    <h4>Best, </h4>
    <h4>Team Restock </h4>
    """

    message = Mail(from_email=MY_ADDRESS, to_emails=CUST_ADDRESS, subject=SUBJECT, html_content=html)
    print("MESSAGE:", type(message))

    try:
        response = client.send(message)
        print("RESPONSE:", type(response))
        print(response.status_code)
        print(response.body)
        print(response.headers)

    except Exception as e:
        print("OOPS", e)
