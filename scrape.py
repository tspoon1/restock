from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#
# INITIALIZE THE DRIVER
#

CHROMEDRIVER_PATH = "c:/Users/timpa/Documents/GitHub/restock/chromedriver.exe" # (or wherever yours is installed)
#chrome_driver_path = "C:\Users\timpa\Documents\geckodriver\chromedriver.exe"

driver = webdriver.Chrome(CHROMEDRIVER_PATH)

# ... OR IN "HEADLESS MODE"...
# options = webdriver.ChromeOptions()
# options.add_argument('--incognito')
# options.add_argument('--headless')
# driver = webdriver.Chrome(CHROMEDRIVER_PATH, chrome_options=options)

#
# NAVIGATE TO GOOGLE.COM...
#

driver.get("https://www.amazon.com/Crest-Enamel-Toothpaste-Advanced-Whitening/dp/B07K11XWXY/ref=sr_1_1_sspa?dchild=1&keywords=toothpaste&qid=1588633934&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUE2S0g1QThLNzM2SlgmZW5jcnlwdGVkSWQ9QTAwNDQzOTdXV1VTNDBMQ0FPMlMmZW5jcnlwdGVkQWRJZD1BMDcwNjI5M1dBUTcyOTFFSTdZJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==")
breakpoint()
print (driver.page_source)
driver.quit()
print(driver.title) #> Google
driver.save_screenshot("search_page.png")

search_input = driver.find_element_by_id("twotabsearchtextbox")
search_input.send_keys("toothpaste")
time.sleep(2)

search_button = driver.find_element_by_xpath('/html/body/div[1]/header/div/div[1]/div[3]/div/form/div[2]/div/input')
search_button.click()
time.sleep(2)

# first_result = driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[2]/div/span[4]/div[2]/div[3]/div/span/div/div/div/div/div[4]/div[1]/div/a/span[1]/span[1]')
# print(first_result.text)

breakpoint()

first_result = driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[2]/div/span[4]/div[1]/div[1]/div/span/div/div/div/div/div[2]/h2/a')
asin = first_result.get_attribute("data-asin")
url = "httpe://www.amazon.com/dp/" + asin
driver.get(url)
price = driver.find_element_by_id("priceblock_ourprice").text
name = driver.find_element_by_id("productTitle").text

print(price)
print(name)
print(url)












#def search_items(item):
#
#    urls = []
#    prices = []
#    names = []
#    for item in items:
#        print(f"Searching for {item}.")
#        self.driver.get(self.amazon_url)
#        search_input = self.driver.find_element_by_id("twotabsearchtextbox")
#        search_input.send_keys(item)
#        time.sleep(5)
#        search_button = self.driver.find_element_by_xpath('/html/body/div[1]/header/div/div[1]/div[3]/div/form/div[2]/div/input')
#        search_button.click()
#        time.sleep(5)

#
# FIND AN ELEMENT TO INTERACT WITH...
# a reference to the HTML element:
# <input title="Search">

#searchbox_xpath = '//input[@title="Search"]'
#searchbox = driver.find_element_by_xpath(searchbox_xpath)
#
##
## INTERACT WITH THE ELEMENT
##
#
#search_term = "Prof Rossetti GitHub"
#searchbox.send_keys(search_term)
#
#searchbox.send_keys(Keys.RETURN)
#print(driver.title) #> 'Prof Rossetti GitHub - Google Search'
#driver.save_screenshot("search_results.png")

#
# ALWAYS QUIT THE DRIVER
#

driver.quit()

