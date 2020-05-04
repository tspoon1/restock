import requests

url = "https://amazon-price1.p.rapidapi.com/priceReport"

querystring = {"asin":"B07Z7H3GJK","marketplace":"US"}

headers = {
    'x-rapidapi-host': "amazon-price1.p.rapidapi.com",
    'x-rapidapi-key': "d30fdebe1bmshce734991bf9ca9bp111549jsn056cb97ab21f"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
 
print(response.text)