from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import gspread
from oauth2client.service_account import ServiceAccountCredentials

from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os

load_dotenv()

def isInStock(product_url):

    inStock = False

    #  IN "HEADLESS MODE  "
    options = webdriver.ChromeOptions()
    options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    options.add_argument('--incognito')
    options.add_argument('--headless')
    options.add_argument("--log-level=3")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=options)

    driver.get(product_url)

    try:
        price = driver.find_element_by_id("priceblock_ourprice").text
        if "$" in price:
            inStock = True
    except Exception as e:
        pass

    driver.quit()

    return inStock

def initSheet():

    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open("Restock").sheet1

    return sheet

def notifyUser(email, url):

    SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")
    SENDGRID_TEMPLATE_ID = os.environ.get("SENDGRID_TEMPLATE_ID")
    MY_ADDRESS = os.environ.get("EMAIL")
    SUBJECT = 'Restock.io: Updates on the availability and price of your product(s)'

    client = SendGridAPIClient(SENDGRID_API_KEY)
    print("CLIENT:", type(client))

    message = Mail(from_email=MY_ADDRESS, to_emails=email, subject=SUBJECT)
    print("MESSAGE:", type(message))

    message.template_id = SENDGRID_TEMPLATE_ID

    message.dynamic_template_data = {
        "name": customer_name
        "human_friendly_timestamp": now.strftime("%d-%m-%Y %I:%M %p"),
        "products": products_list
        }

    try:
        response = client.send(message)
        print("RESPONSE:", type(response))
        print(response.status_code)
        print(response.body)
        print(response.headers)

    except Exception as e:
        print("OOPS", e)
        print("--------ERROR SENDING---------")
        print(f"The row deleted but that didn't send correctly was {email}")
        print(url)
        print("--------ERROR SENDING---------")


if __name__ == "__main__":

    sheet = initSheet()
    email = "temp@email.com"

    emailList = sheet.col_values(1)[1:]
    urlList = sheet.col_values(2)[1:]
    rowNumber = 2

    for email, url in zip(emailList, urlList):
        if isInStock(url):
            notifyUser(email, url)
            sheet.delete_row(rowNumber)
        rowNumber += 1