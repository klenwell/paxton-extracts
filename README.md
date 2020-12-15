# Paxton 365 Extract
This script was created specifically to assist an independent consultant, my sister, with her billing. It uses the Microsoft 365 API to pull data like emails and calendars to detail and verify client invoicing.

Because my sister works primarily within the Microsoft ecosystem (much to my chagrin), we needed to devise a quick and dirty way for her to reliably execute it. To do so, we took advantage of shared consoles in Python Anywhere. The install section outlines installation with that context in mind.

## Requirements
- Python 3.4+
- Microsoft 365 Account
- App registered with Azure Portal
- App client / secret IDs for API access

## Install
- Create a virtualenv
- Clone the repository
- Install pip requirments
- Set up secrets file with Azure IDs

## Usage

    python main.py
