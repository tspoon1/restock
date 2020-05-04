import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.com/AUKEY-Ethernet-Delivery-Charging-MacBook/dp/B07Z7H3GJK/ref=sr_1_3?crid=2V4KZOBILXKOV&dchild=1&keywords=aukey+usb+c+hub&qid=1588036771&s=electronics&sprefix=aukey+usb+c%2Celectronics%2C1091&sr=1-3"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}

page = requests.get(URL, headers = headers)

soup = BeautifulSoup(page.content, "html.parser")

print(soup.prettify())
