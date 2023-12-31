"""Service module

This is a module to create the services that will be used by.
"""
from os import environ as env
import xml.etree.ElementTree as et
from twilio.rest import Client
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
load_dotenv()

account_sid = env['ACCOUNT_SID']
auth_token = env['AUTH_TOKEN']
twilio_phone_number = env['TWILIO_PHONE_NUMBER']
phone_number = env['PHONE_NUMBER']
APPLE_KIT_STRING = "AppleWebKit/537.36 (KHTML, like Gecko) "
BROWSERS = "Chrome/81.0.4044.138 Safari/537.36"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " + APPLE_KIT_STRING + BROWSERS,
    'Accept': '*/*', 
    'Accept-Encoding': 'gzip, deflate, br', 
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8'
}

def send_sms(body):
    """
    This function create a sms client.
    """
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_=twilio_phone_number,
        body=body,
        to=phone_number
    )
    print(message.sid)

def scraper(url):
    """
    This function create a scraper dom by url.
    """
    response = requests.get(url, headers=header, timeout=5)
    soup = BeautifulSoup(response.content, 'html.parser')
    dom = et.parse(str(soup))
    return dom
