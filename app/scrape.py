#scrape.py

#importing key packages/ modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

import gspread
from oauth2client.service_account import ServiceAccountCredentials

#import other key functions
from app.email_service import send_email

def isInStock(product_url, chromeDriverPath):

    inStock = False

    #  IN "HEADLESS MODE  "
    #LOGGER.setLevel(logging.WARNING)
    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')
    options.add_argument('--headless')
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(CHROMEDRIVER_PATH, options=options)

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

def addNewRow(row):
    sheet.insert_row(row, 2)


#error message printing function
def print_input_err_message():
    """
        This function prints an error message and then exits. It occurs whenever there is input validation errors or HTTP request errors.

        @param: none.

    """

    print("")
    print("OOPS, the link you entered does not work; please input links in the following format: https://amazon...")
    print("Please try run the program again. Thank you!")
    print("")
    exit()


if __name__ == "__main__":

    #import statements
    from dotenv import load_dotenv
    from sendgrid import SendGridAPIClient
    from sendgrid.helpers.mail import Mail

    load_dotenv()

    #defining key variables
    now = datetime.now()
    CHROMEDRIVER_PATH = "c:/Users/timpa/Documents/GitHub/restock/chromedriver.exe"

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
    url = input("Please input the amazon URL for the product that you would which to keep tabs on: ")

    #quick validation
    if "amazon" in url:
        print("Great, we're looking into it right now... \n")
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
            print("Whoops, please enter a valid email.")
            email = input("-->")

        print("Adding your request to our database...")
        newRow = [email, url]
        addNewRow(newRow)

        print("Thanks for adding your item to Restock!\n")


    #PART XXX: emailing the user about product info

    #TO DO : CONNECT EMAIL HERE
    


    #concluding statement to thank the client for using the service
    print("")
    print("")
    print("Thank you for using Restock.io! We hope you got the information you were looking for \n")
    print("We look forward to keeping you updated on the products that you care about!\n")
    print("If you think there is a way we can improve our service, contact us at customerrelations@restock.io")
    print("")
    