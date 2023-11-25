# Amazon price monitor

## Description
It's a python application that helps you save money on black friday.

Currently supported E-commerce websites : Amazon BR. 

It is built using Python, Twilio and Beautiful Soup. 

## Working
The application consists in monitoring price drops for Amazon Brasil Products every one hour and send alert drops via sms.

## Installation and Usage

1. Clone the project on your local system using: `git clone https://github.com/Evoney/amazon-price-monitor.git`

2. Install the dependencies: `pip install -r requirements.txt`

3. Setup environment variables in `.env` file.

   Notes : 
   1. Add 'ACCOUNT_SID', 'AUTH_TOKEN' for Twilio Api Client.
   2. Add 'TWILIO_PHONE_NUMBER', 'PHONE_NUMBER' after setting up twilio and your phone number profile.

4. Fill the `links.txt` file with Amazon Products Url.

5. Run using `python main.py`

## Notes

1. You would need to authenticate your Twilio client using your own account by following docs instruction after running `main.py` for first time usage.

- [TWILIO](https://www.twilio.com/docs/messaging) API reference documentation and quickstarts with Twilio.

## Utilities

- [x] Functionality for price monitor for Amazon Brasil
- [ ] Functionality for price monitor for Mercado Livre Brasil
- [x] Notification via SMS

## Contributing

This repository is currently under development. If you want to contribute please fork the repository and get your hands dirty, and make the changes as you'd like and submit the Pull request.


  
  
