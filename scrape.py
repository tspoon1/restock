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
CHROMEDRIVER_PATH = "c:/Users/timpa/Documents/GitHub/restock/chromedriver.exe"
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







    




#print(driver.title) #> Google
#driver.save_screenshot("search_page.png")
#
#search_input = driver.find_element_by_id("twotabsearchtextbox")
#search_input.send_keys("toothpaste")
#time.sleep(2)
#
#search_button = driver.find_element_by_xpath('/html/body/div[1]/header/div/div[1]/div[3]/div/form/div[2]/div/input')
#search_button.click()
#time.sleep(2)
#
## first_result = driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[2]/div/span[4]/div[2]/div[3]/div/span/div/div/div/div/div[4]/div[1]/div/a/span[1]/span[1]')
## print(first_result.text)
#
#breakpoint()
#
#first_result = driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[2]/div/span[4]/div[1]/div[1]/div/span/div/div/div/div/div[2]/h2/a')
#asin = first_result.get_attribute("data-asin")
#url = "httpe://www.amazon.com/dp/" + asin
#driver.get(url)
#price = driver.find_element_by_id("priceblock_ourprice").text
#name = driver.find_element_by_id("productTitle").text
#
#print(price)
#print(name)
#print(url)
#
#
#
#
#
#
#
#
#
#
#
#
##def search_items(item):
##
##    urls = []
##    prices = []
##    names = []
##    for item in items:
##        print(f"Searching for {item}.")
##        self.driver.get(self.amazon_url)
##        search_input = self.driver.find_element_by_id("twotabsearchtextbox")
##        search_input.send_keys(item)
##        time.sleep(5)
##        search_button = self.driver.find_element_by_xpath('/html/body/div[1]/header/div/div[1]/div[3]/div/form/div[2]/div/input')
##        search_button.click()
##        time.sleep(5)
#
##
## FIND AN ELEMENT TO INTERACT WITH...
## a reference to the HTML element:
## <input title="Search">
#
##searchbox_xpath = '//input[@title="Search"]'
##searchbox = driver.find_element_by_xpath(searchbox_xpath)
##
###
### INTERACT WITH THE ELEMENT
###
##
##search_term = "Prof Rossetti GitHub"
##searchbox.send_keys(search_term)
##
##searchbox.send_keys(Keys.RETURN)
##print(driver.title) #> 'Prof Rossetti GitHub - Google Search'
##driver.save_screenshot("search_results.png")
#
##
## ALWAYS QUIT THE DRIVER
##
#
#driver.quit()
#
#