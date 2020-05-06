## The Project
An application that aims to help users stay up to date on the prices/ availability of the products they are looking for. Given uncertain times such as now, where COVID-19 has forced the supply of certain key products to change in price or become unavailable, there is a high demand for the updating of key product price and availability data. Our application aims to keep users informed on what is happening with their key products in a friendly and easy manner. Say goodbye to checking Amazon 24/7 for toilet paper :)


## Prerequisites:
- Anaconda 3.7 <br />
- Python 3.7 <br />
- Pip

## Required Python Packages & Modules:
- dotenv 
- os 
- datetime
- sendgrid
- flask
- gunicorn
- gspread
- oauth2client
- bs4
- selenium
- pytest

## Installation:
In order to set this project up, please download this repo and write into the command line: <br />
    - git clone git@github.com:tspoon1/restock <br />
    - cd restock/ <br />

Proceed to download the following packages: <br />
```sh
pip install -r requirements.txt
```
<br />


## Setting up the Environment:
```sh
conda create -n restock-env python=3.7 # (first time only) <br />
conda activate restock-env 
```
<br />

## Set Up
In addition to what was said above, make sure to configure your env to fit the required variables: <br />
- Sendgrid API KEY <br />
- Sendgrid API TEMPLATE <br />
- An email address to use for sending and receiving emailed alerts <br />


### The `sendgrid` Package

The `sendgrid` package provides  emailing capabilities via the [SendGrid Email Delivery Service](https://sendgrid.com/solutions/email-api/). :mailbox_with_mail: :envelope:

### Installation

From within a virtual environment, install `sendgrid`, if necessary:

```sh
pip install sendgrid==6.0.5
```

First, [sign up for a free account](https://signup.sendgrid.com/), then click the link in a confirmation email to verify your account. Then [create an API Key](https://app.sendgrid.com/settings/api_keys) with "full access" permissions.

To setup the usage examples below, store the API Key value in an environment variable called `SENDGRID_API_KEY`. Also set an environment variable called `MY_EMAIL_ADDRESS` to be the email address you just associated with your SendGrid account (e.g. "johndoe@gmail.com").

For information on how to obtain a Sendgrid API key and tempate (it's very easy by the way so don't be too concerned), check out these three explanatory links: <br />
- https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/packages/sendgrid.md
- https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/packages/sendgrid.md#email-templates
- https://github.com/prof-rossetti/intro-to-python/blob/master/exercises/emails-with-templates/send_email.py

## Deploying the local Flask version to online server (powered by Heroku)
After demonstrating the ability to successfully run the web app locally, deploy the web service by uploading the source code onto a remote server:

```sh
git push heroku master
```
If you are unfamiliar with the code above, and/ or you have never used Heroku before, click the link below for a comprehensive guide (from Professor Rossetti) on Heroku, setting up an account, and getting it all running:
https://github.com/prof-rossetti/intro-to-python/blob/master/exercises/web-service/deploying.md

After entering the command line code above, you'll need to create a special file called the "Procfile" in the root directory. This file is key because it essentially coordiantes with the Heroku server on which command to invoke to run the app:

```sh
web: gunicorn "web_app:create_app()"
```

Save the "Procfile" and make a commit before re-attempting to deploy your app to the server.

```sh
git push heroku master
```

View the server logs and troubleshoot as necessary until you're able to see the application's home page in the browser.

```sh
heroku logs --tail
```

## Usage:
Run the recommendation script: <br />
- python app/main_script.py  <br />

## User Instructions:

In terms of application usage, there are two ways in which this application can be used:
- online web app version (powered through Heroku)
- command line web app version (powered by Flask)

### Online Version

COMING SOON...

Click through to where you can enter your details (Name) and then the link of the product you wish to track on Amazon.
The program will come back with one of two respones: either the product is in stock and therefore the program will end there, or it is not in stock. If it is the latter, the application will request your email. If you wish to receive updates every once in a while, enter your email and the application will email you until the product becomes available, in which case you will then be removed from the email list.


### Command line version
Run the program given the instructions above and you will first see a welcoming message. Enter your name and then the link of the product you wish to track on Amazon. Just like above, the program will come back with one of two respones: either the product is in stock and therefore the program will end there, or it is not in stock. If it is the latter, the application will request your email. If you wish to receive updates every once in a while, enter your email and the application will email you until the product becomes available, in which case you will then be removed from the email list.

#### Flask Instructions
Depending on the way a Flask app is organized, the run command will differ, but based on the provided organizational structure (with the `create_app()` function in the "web_app/\_\_init__.py" file), the following command should run web application locally so you can view it in a browser at localhost:5000:

```sh
# Mac:
FLASK_APP=web_app flask run

# Windows:
export FLASK_APP=web_app # first time, to set the env var
flask run # subsequent times
```
Following this, proceed to visit localhost:5000 in the browser!

## Testing

Run the test(s):

```sh
pytest
```


## Code Climate Software Check:
TODO