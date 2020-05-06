from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

import gspread
from oauth2client.service_account import ServiceAccountCredentials

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


url = "https://www.amazon.com/Nintendo-Switch-Neon-Blue-Joy%E2%80%91/dp/B07VGRJDFY/ref=sr_1_3?crid=IY3K5B823UOZ&dchild=1&keywords=nintendo+switch&qid=1588716182&sprefix=nintend%2Caps%2C159&sr=8-3"
CHROMEDRIVER_PATH = "/app/chromedriver.exe"
sheet = initSheet()

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