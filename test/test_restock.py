from app.scrape import is_valid
from app.email_service import send_email

def test_is_valid():
    
    url = "https://www.amazon.com/Nintendo-Switch-Neon-Blue-Joy%E2%80%91/dp/B07VGRJDFY/ref=sr_1_3?crid=IY3K5B823UOZ&dchild=1&keywords=nintendo+switch&qid=1588716182&sprefix=nintend%2Caps%2C159&sr=8-3"
    url_wrong = "https://www.youtube.com"

    #Should result in Correct statement
    assert is_valid(url) == True

    #Should result in an Incorrect statement
    assert is_valid(url_wrong) == False

def test_send_email():

    name = "John"
    email = "jack@longarzo.com"
    product = "https://www.amazon.com/Nintendo-Switch-Neon-Blue-Joy%E2%80%91/dp/B07VGRJDFY/ref=sr_1_3?crid=IY3K5B823UOZ&dchild=1&keywords=nintendo+switch&qid=1588716182&sprefix=nintend%2Caps%2C159&sr=8-3"
    availability = "Available"

    #Looking for thar successfully sent email, which should return a 202 code in the output
    assert "202" in send_email(name, email, product, availability)

