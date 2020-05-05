#main_script.py


#import certain modules/ packages
import requests
import os
import csv 


#error message printing function
def print_input_err_message():
    """
        This function prints an error message and then exits. It occurs whenever there is input validation errors or HTTP request errors.

        @param: none.

    """

    print("")
    print("OOPS, the link you entered does not work; please input links in the following format: https://amazon...")
    print("Please try run the program again. Thank you!")
    print("")
    exit()


if __name__ == "__main__":

    #import statements
    from dotenv import load_dotenv

    load_dotenv()

    #PART 1: Program intro and user input collection
    print("")
    print("Welcome to Restock.io, a tool for you to see whether your favorite Amazon products , or perhaps those items that you really need now, are available and, if so, for what price\n")
    print("Our mission is to remove all the effort and stress of having to regularly hunt through Amazon for your products!\n")
    print("At a high level, what the application does is takes in the links of the Amazon products you want to keep a watch out for")
    print("Check's for their prices and availability at regular intervals, and then maintains communication with you (via email) to update you on product availability and price\n")
    print("In tough times like now, where product shortages are common, we hope to alievate some of that stress and automate the looking for you!\n")

    #define list + url
    url_list = []
    user_url = ""

    #customer email input
    print("")
    CUST_ADDRESS = input("Please input your email to receieve alerts for product availability and price information: ")
    print("")
    print("")

    while user_url != "DONE":
        user_url = input(print("Please enter the Amazon link of the object "))
        #some quick prelimenary input validation (in order to save time of issuing a get request)

        #request check can be run here
        check == True
        if check == True:
            url_list.append(user_url)
        else:
            print_input_err_message()

    #remove the DONE
    url_list.pop()
    

    #PART 2: taking in the links and running the scraper to obtain the necessary information/ data

    for l in url_list:

        #TO DO
        #Tim scraper thing



    #PART XXX: emailing the user about product info

    #TO DO make this all automatable

    #get variables from .env
    SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")
    SENDGRID_TEMPLATE_ID = os.environ.get("SENDGRID_TEMPLATE_ID")
    MY_ADDRESS = os.environ.get("EMAIL")
    SUBJECT = 'Restock.io: Updates on the availability and price of your product(s)'

    client = SendGridAPIClient(SENDGRID_API_KEY)
    print("CLIENT:", type(client))

    message = Mail(from_email=MY_ADDRESS, to_emails=CUST_ADDRESS, subject=SUBJECT)
    print("MESSAGE:", type(message))

    message.template_id = SENDGRID_TEMPLATE_ID

    message.dynamic_template_data = {
        "symbol": s,
        "human_friendly_timestamp": now.strftime("%d-%m-%Y %I:%M %p"),
        "movement": movement_str
        }# or construct this dictionary dynamically based on the results of some other process :-D

    try:
        response = client.send(message)
        print("RESPONSE:", type(response))
        print(response.status_code)
        print(response.body)
        print(response.headers)

    except Exception as e:
        print("OOPS", e)


    #concluding statement to thank the client for using the service
    print("")
    print("")
    print("Thank you for using Restock.io! We hope you got the information you were looking for \n")
    print("We look forward to keeping you updated on the products that you care about!\n")
    print("If you think there is a way we can improve our service, contact us at customerrelations@restock.io")
    print("")
    



