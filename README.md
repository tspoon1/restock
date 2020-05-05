## The Project
An application that aims to help users stay up to date on the prices/ availability of the products they are looking for. Given uncertain times such as now, where COVID-19 has forced the supply of certain key products to change in price or become unavailable, there is a high demand for the updating of key product price and availability data. Our application aims to keep users informed on what is happening with their key products in a friendly and easy manner. Say goodbye to checking Amazon 24/7 for toilet paper :)


## Prerequisites:
- Anaconda 3.7 <br />
- Python 3.7 <br />
- Pip

## Required Python Packages & Modules:
- datetime <br />
- dotenv <br />
- os <br />
- sendgrid <br />

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
conda create -n restock-env python=3.7 # (first time only) <br />
conda activate restock-env <br />
<br />

## Set Up
n addition to what was said above, make sure to configure your env to fit the required variables: <br />
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

## Usage:
Run the recommendation script: <br />
- python app/main_script.py  <br />

## User Instructions:

TODO

## Testing

Run the test(s):

```sh
pytest
```
