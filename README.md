## Restock.io
The application that aims to help users stay up to date on the prices/availability of the products they are looking for. Given uncertain times such as now, where COVID-19 has forced the supply of certain key products to change in price or become unavailable, there is a high demand for the updating of key product price and availability data. Our application aims to keep users informed on what is happening with their key products in a friendly and easy manner. Say goodbye to checking Amazon 24/7 for toilet paper :)


## Prerequisites:
- Anaconda 3.7 <br />
- Python 3.7 <br />
- Pip

## Required Python Packages & Modules:
- python-dotenv 
- os 
- datetime
- sendgrid
- flask
- gunicorn
- gspread
- oauth2client
- selenium
- pytest

## Setting up the Environment:
Before installing the requirements to run this, please make a virtual environment for your restock programs to live in by doing the following:
```sh
conda create -n restock-env python=3.7 # (first time only) <br />
conda activate restock-env 
```
<br />

## Installation:
In order to set this project up, please download this repo and write into the command line: <br />
```
git clone git@github.com:tspoon1/restock <br />
cd restock/ <br />
```
Proceed to download the following packages: <br />
```sh
pip install -r requirements.txt
```
<br />

## Set Up
In addition to what was said above, make sure to configure your env to fit the required variables: <br />
- A SENDGRID_API_KEY <br />
- An email address to use for sending and receiving emailed alerts stored in EMAIL<br />


### The `sendgrid` Package

The `sendgrid` package provides  emailing capabilities via the [SendGrid Email Delivery Service](https://sendgrid.com/solutions/email-api/). :mailbox_with_mail: :envelope:

#### Installation if you do not have it already

First, [sign up for a free account](https://signup.sendgrid.com/), then click the link in a confirmation email to verify your account. Then [create an API Key](https://app.sendgrid.com/settings/api_keys) with "full access" permissions.

To setup the usage examples below, store the API Key value in an environment variable called `SENDGRID_API_KEY`. Also set an environment variable called `MY_EMAIL_ADDRESS` to be the email address you just associated with your SendGrid account (e.g. "johndoe@gmail.com").

For information on how to obtain a Sendgrid API key and tempate (it's very easy by the way so don't be too concerned), check out these three explanatory links: <br />
- https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/packages/sendgrid.md
- https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/packages/sendgrid.md#email-templates
- https://github.com/prof-rossetti/intro-to-python/blob/master/exercises/emails-with-templates/send_email.py

## Deploying the local Flask version to online server (powered by Heroku)
If you are unfamiliar with or you have never used Heroku before, click the link below for a comprehensive guide (from Professor Rossetti) on Heroku, setting up an account, and getting it all running:
https://github.com/prof-rossetti/intro-to-python/blob/master/exercises/web-service/deploying.md

###Some Key Highlights from the Guide (Professor Rossetti's words)
If you haven't yet done so, [install the Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install), and make sure you can login and list your applications.

```sh
heroku login # just a one-time thing when you use heroku for the first time

heroku apps # at this time, results might be empty-ish
```

Before we copy the source code to the remote server, we need to configure the server's environment in a similar way we configured our local environment.

Instead of using a ".env" file, we will directly configure the server's environment variables by either clicking "Reveal Config Vars" from the "Settings" tab in your application's Heroku dashboard



After creating a heroku app and configuring your env-variables whether through a CLI or the heroku website as outlined above, you'll need to utilize the special file called the "Procfile" in the root directory. This file is key because it essentially coordiantes with the Heroku server on which command to invoke to run the app.

Make a commit to the heroku app and utilize the already existing Procfile to launch the application.

```sh
git push heroku master
```

View the server logs and troubleshoot as necessary until you're able to see the application's home page in the browser.

```sh
heroku logs --tail
```

## Google Sheet Setup:
After you can see your version of the Restock.io app running perfectly, you are almost there! Once you have done this, all you have to do is set up your google sheet.

You will need to utilize the gspread, Google Sheets API, in order to get a backend up and running. If you have never done this, below are a few awesome references to get going:
- https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/packages/gspread.md
- https://github.com/googleapis/google-api-python-client
- https://developers.google.com/api-client-library/python/
- https://developers.google.com/sheets/api/guides/authorizing

### Sheet Basics
Ensure that your client_secret.json is in your root directory, and you have created a sheet that has the following contents in the following cells:
```
A1 = 'email'
B1 = 'url'
```

## Testing
After doing all of the above, your front end should be able handle form inputs and store them appropriately in the google sheet you have made. If not, this may be a good time to utilize the test suit we have written for each one of our tests. Perform them by typing the following when in the root directory:
```
pytest
```

## Code Climate Software Check:
<a href="https://codeclimate.com/github/jsoles7/restock/maintainability"><img src="https://api.codeclimate.com/v1/badges/8b8408b02ef475d53613/maintainability" /></a>


## To Restock, or not to Restock
Upon completion of everything above, you are good to go! Just make sure to keep an eye out for our v3.0 to release, where the google sheet will be automatically run-through and checked regularly by a herkou scheduled script. But for now, just type the following into your CLI a couple times a day to keep your own Restock users happy!
```
python app/email_runner.py
```

## Goodluck and thank you for using Restock.io!
#### The Restock team <3
