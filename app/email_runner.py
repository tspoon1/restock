from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import gspread
from oauth2client.service_account import ServiceAccountCredentials

from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os
from datetime import datetime

from restock import isInStock, initSheet, send_email

load_dotenv()

if __name__ == "__main__":

    sheet = initSheet()
    email = "temp@email.com"

    emailList = sheet.col_values(1)[1:]
    urlList = sheet.col_values(2)[1:]
    rowNumber = 2

    for email, url in zip(emailList, urlList):
        if isInStock(url):
            send_email(email, url, "available")
            sheet.delete_rows(rowNumber)
        else:
            rowNumber += 1