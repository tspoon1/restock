from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import gspread
from oauth2client.service_account import ServiceAccountCredentials

from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os

from restock import initSheet, send_email

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
    print(driver.page_source)

    try:
        price = driver.find_element_by_id("priceblock_ourprice").text
        if "$" in price:
            inStock = True
    except Exception as e:
        pass

    driver.quit()

    return inStock

if __name__ == "__main__":

    sheet = initSheet()
    email = "temp@email.com"

    emailList = sheet.col_values(1)[1:]
    urlList = sheet.col_values(2)[1:]
    rowNumber = 2
    print(emailList)
    print(urlList)

    for email, url in zip(emailList, urlList):
        print(isInStock(url))
        if isInStock(url):
            send_email(email, url, "available")
            sheet.delete_row(rowNumber)
        rowNumber += 1