from app.restock import is_valid, send_email, addNewRow, initSheet

def test_is_valid():
    
    url = "https://www.amazon.com/Nintendo-Switch-Neon-Blue-Joy%E2%80%91/dp/B07VGRJDFY/ref=sr_1_3?crid=IY3K5B823UOZ&dchild=1&keywords=nintendo+switch&qid=1588716182&sprefix=nintend%2Caps%2C159&sr=8-3"
    url_wrong = "https://www.youtube.com"

    #Should result in Correct statement
    assert is_valid(url) == True

    #Should result in an Incorrect statement
    assert is_valid(url_wrong) == False

def test_send_email():

    email = "jack@longarzo.com"
    product = "https://www.amazon.com/Nintendo-Switch-Neon-Blue-Joy%E2%80%91/dp/B07VGRJDFY/ref=sr_1_3?crid=IY3K5B823UOZ&dchild=1&keywords=nintendo+switch&qid=1588716182&sprefix=nintend%2Caps%2C159&sr=8-3"
    availability = "Available"

    #Looking for thar successfully sent email, which should return a 202 code in the output
    assert send_email(email, product, availability) == "sent"

def test_addNewRow():
    email = "jack@longarzo.com"
    product_url = "https://www.amazon.com/Nintendo-Switch-Neon-Blue-Joy%E2%80%91/dp/B07VGRJDFY/ref=sr_1_3?crid=IY3K5B823UOZ&dchild=1&keywords=nintendo+switch&qid=1588716182&sprefix=nintend%2Caps%2C159&sr=8-3"
    test_row = [email, product_url]

    #should return the new row that was just added by grabbing the 2nd row
    assert addNewRow(test_row) == test_row

    sheet = initSheet()
    sheet.delete_rows(2)
