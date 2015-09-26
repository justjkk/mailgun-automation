# README
Mailgun automation scripts

## Setup

* Copy .credentials.sample into .credentials
* Set the correct values in .credentials
* Install python dependencies from requirements.txt

## Usage

* source .credentials  # Sets the mailgun credentials as environment variables

### Printing the bounce list
* python get_bounces.py

### Clearing the bounce list
* python get_bounces.py | python unbounce.py
