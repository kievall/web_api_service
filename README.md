#  Favorite Restaurants Mock API

The Mock API has been verified with:
- Python 3.6.4
- pip 18.0

### DEMO
[![Video]()](https://youtu.be/gNy5iNGBnAU "DEMO - Click to Watch!")

## Prerequisites

The mock API requires Python 3 and pip installed. To verify if you have both packages installed run the following commands:

`python3 --version`
`pip --version`

If pip and Python 3 are installed you should see version of each package. Otherwise you'll see an error message.

If you do not have Python 3 and pip installed, use your operating system package manager to install both tools.
On Mac OS you could use brew:

`brew install python`


## Install Requirements

`pip install -r requirements.txt`

If there is a permissions error add a `--user` flag to the end of the command.

If there is an SSL error, for example:

"Could not fetch URL https://pypi.python.org/simple/faker/: There was a problem confirming the ssl certificate:
[SSL: TLSV1_ALERT_PROTOCOL_VERSION] tlsv1 alert protocol version (_ssl.c:590) - skipping"

Try to upgrade pip using one of the following commands:

`pip install -U pip`
`curl https://bootstrap.pypa.io/get-pip.py | python3`
`pip2 install --upgrade pip`

## To Run

Add this directory to your python path (replace with your own local path)

`export PYTHONPATH=${PYTHONPATH}:$(pwd)`

Then start up the app.

`python3 -m favorite_restaurants.api`

## To Verify

Verify the app is up and running by opening a new window and running the command:

`curl -vv http://localhost:5000/favorite_restaurants`

It should return a 200 response.

## Testing Guidelines

Note that the `/favorite_restaurants` endpoint will require an "auth token" which will be returned after a successful
post to the `/login` endpoint. For more details refer to the documentation.
