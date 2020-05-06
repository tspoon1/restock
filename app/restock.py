#restock.py

#importing key packages/ modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials

import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from datetime import datetime
load_dotenv()

def isInStock(product_url):

    """
        isInStock utilizes selenium to grab an amazon.com url specified by the user and
        searched for the tag which amazon uses to specify price. If it doesn't have this tag with a
        $ inside of it, we return false to the program calling the function.

        @param: the product URL in string format an the path of the Chrome Driver, which is in string format too
        @param: the path to the chromeDriver.exe that makes selenium launch
        
        @return: boolean (based on whether it is in stock or not)

    """

    inStock = False

    #  IN "HEADLESS MODE  "
    CHROMEDRIVER_PATH = "c:/Users/timpa/Documents/GitHub/restock/chromedriver.exe"
    options = webdriver.ChromeOptions()
    #options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    options.add_argument('--incognito')
    options.add_argument('--headless')
    options.add_argument("--log-level=3")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=options)

    driver.get(product_url)
    #print(driver.page_source)

    try:
        #scrape the HTML code and check for the price block. If there is a $ in the block, a price is given and the product 
        # is available; if not, its not there
        price = driver.find_element_by_id("priceblock_ourprice").text
        if "$" in price:
            inStock = True
    except Exception as e:
        pass

    driver.quit()

    #return the boolean that will be used to alert the client
    return inStock

def initSheet():
    """
        This function makes use of the Google Sheets API to provide access to Restock's customer database google sheet.
        It makes use of Google Sheet's integration to bring in access to a local variable, which it then serves as an access window
        for data transfer. It returns the access to this sheet

        @param: none

    """
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open("Restock").sheet1

    return sheet

def addNewRow(row):
    """
        This function adds a new row in the Google sheet in order for new customer data entry. Note that it calls the initSheet()
        function within the function.

        @param: given row data, which is a list item containing the email and link

    """
    sheet = initSheet()
    sheet.insert_row(row, 2)
    return sheet.row_values(2)

#error message printing function
def print_input_err_message():
    """
        This function prints an error message and then exits. It occurs whenever there is input validation errors.

        @param: none.

    """

    print("")
    print("OOPS, the link you entered does not work; please input links in the following format: https://amazon...")
    print("Please try run the program again. Thank you!")
    print("")
    exit()

def is_valid(url):

    """
        This function validates the url. Returns True is valid and False if not

        @param: url, the string variable that has the link given by the customer

    """
    #quick validation
    if "www.amazon.com" in url and "https://" in url:
        return True
    else:
        return False

def send_email(customer_address, product_url, availability):

    """
        This function makes use of the SendGrid API to formulate an email that can be sent to the customer, notifying them of the 
        current availability of their product. The instructions to sendgrid installation can be found in the README. It takes the four
        inputs below and uses a custom HTML template to formulate the email. Note that API KEY and the sending email address are 
        kept undisclosed in the .env file

        @param: customer_name (a string that contains the customer's name)
        @param: customer_address (a string that contains the customer's email)
        @param: product_url (the link of the product that the customer gave, in string format)
        @param: availability (a string that informs the customer of if the product is available or not)

    """
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

    <h4>Dear Valued Restock Customer,</h4>
    <p>Date: {date_and_time}</p>


    <p>We hope this email finds you well. You are receiving this notification as part of your product monitoring subscription with Restock.io.</p>

    <p>Below, we have listed the product you wanted to watch: {product_url}</p>

    <p>Your product is currently {availability}.
    <p>Thank you for trusting us as your shopping helper! Please give us a shout by sharing this service with your friends/ family: we are here to help!</p>


    <h4>Best, </h4>
    <h4>Team Restock </h4>
    """

    message = Mail(from_email=MY_ADDRESS, to_emails=CUST_ADDRESS, subject=SUBJECT, html_content=html)
    print("MESSAGE:", type(message))

    try:
        response = client.send(message)
        print(response.status_code)
        if response.status_code == 202: return "sent"
    except Exception as e:
        print("OOPS", e)

if __name__ == "__main__":

    #starting a sheet
    sheet = initSheet()

    #PART 1: Program intro and user input collection
    print("")
    print("Welcome to Restock.io, a tool for you to see whether your favorite Amazon products , or perhaps those items that you really need now, are available and, if so, for what price\n")
    print("Our mission is to remove all the effort and stress of having to regularly hunt through Amazon for your products!\n")
    print("At a high level, what the application does is takes in the links of the Amazon products you want to keep a watch out for")
    print("Check's for their prices and availability at regular intervals, and then maintains communication with you (via email) to update you on product availability and price\n")
    print("In tough times like now, where product shortages are common, we hope to alievate some of that stress and automate the looking for you!\n")


    #asking for user input
    print("")
    print("")
    name = input("Please write your name: ")
    url = input("Please input the amazon URL for the product that you would which to keep tabs on: ")

    #run the function to check validity
    validity = is_valid(url)
    if validity == True:
        print(f"{name}, Adding your request to our database...")
    else:
        print_input_err_message()


    url = "https://www.amazon.com/Nintendo-Switch-Neon-Blue-Joy%E2%80%91/dp/B07VGRJDFY/ref=sr_1_3?crid=IY3K5B823UOZ&dchild=1&keywords=nintendo+switch&qid=1588716182&sprefix=nintend%2Caps%2C159&sr=8-3"
    


    #print(isInStock(url, CHROMEDRIVER_PATH))
    email = ""

    if isInStock(url, CHROMEDRIVER_PATH):
        print("Oh, your item is in stock. Maybe try a different link!")
    else:
        print("Looks like your item is indeed out of stock.")
        print("If you would like us to send you an email when")
        print("your item is back in stock, enter it below!")
        email = input("-->")

        while ("@" not in email):
            print("Whoops, please enter a valid email:")
            email = input("-->")

        print("Adding your request to our database...")
        newRow = [email, url]
        addNewRow(newRow)

        print(f"Thanks for adding your item to Restock, {name}!\n")


    #PART XXX: emailing the user about product info

    #TO DO : CONNECT EMAIL HERE



    #concluding statement to thank the client for using the service
    print("")
    print("")
    print("Thank you for using Restock.io! We hope you got the information you were looking for \n")
    print("We look forward to keeping you updated on the products that you care about!\n")
    print("If you think there is a way we can improve our service, contact us at customerrelations@restock.io")
    print("")

