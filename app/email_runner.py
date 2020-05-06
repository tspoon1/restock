from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import gspread
from oauth2client.service_account import ServiceAccountCredentials

from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os
import datetime

from scrape import isInStock, initSheet

load_dotenv()

def notifyUser(email, url):

    load_dotenv()
    #get variables from .env
    SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")
    MY_ADDRESS = os.environ.get("EMAIL")

    now = datetime.datetime.now()
    date_and_time = now.strftime("%d-%m-%Y %I:%M %p")
    CUST_ADDRESS = email
    SUBJECT = 'Restock.io: Updates on the availability and price of your product(s)'


    client = SendGridAPIClient(SENDGRID_API_KEY)
    print("CLIENT:", type(client))

    html = f"""

    <img src="https://media1.s-nbcnews.com/j/newscms/2018_29/2473831/180622-amazon-mc-1124_36a8ba8a051fde1141e943390ac804f9.fit-760w.JPG">

    <h4>Dear Restock user,</h4>
    <p>Date: {date_and_time}</p>


    <p>We hope this email finds you well. You are receiving this notification as part of your product monitoring subscription with Restock.io.</p>

    <p>Below, we have listed the product you wanted to watch</p>

    <p>Your product is currently available! Make sure you revisit your url before it runs out: {url}</p>
    <p>Thank you for trusting us as your shopping helper! Please give us a shout by sharing this service with your friends/ family: we are here to help.</p>


    <h4>Best, </h4>
    <h4>Team Restock </h4>
    """

    message = Mail(from_email=MY_ADDRESS, to_emails=CUST_ADDRESS, subject=SUBJECT, html_content=html)
    print("MESSAGE:", type(message))

    try:
        response = client.send(message)
        print(response.status_code)

    except Exception as e:
        print("OOPS", e)

if __name__ == "__main__":

    sheet = initSheet()
    email = "temp@email.com"

    emailList = sheet.col_values(1)[1:]
    urlList = sheet.col_values(2)[1:]
    rowNumber = 2

    for email, url in zip(emailList, urlList):
        if isInStock(url):
            notifyUser(email, url)
            sheet.delete_rows(rowNumber)
        else:
            rowNumber += 1