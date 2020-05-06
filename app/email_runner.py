#app/email_runner.py
from restock import isInStock, initSheet, send_email

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