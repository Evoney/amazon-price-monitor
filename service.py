from twilio.rest import Client
import requests
from bs4 import BeautifulSoup
from lxml import etree as et
from os import environ as env
from dotenv import load_dotenv
load_dotenv()

account_sid = env['ACCOUNT_SID']
auth_token = env['AUTH_TOKEN']
twilio_phone_number = env['TWILIO_PHONE_NUMBER']
phone_number = env['PHONE_NUMBER']

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8'
}

def send_sms(body):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_=twilio_phone_number,
        body=body,
        to=phone_number
    )
    print(message.sid)

def scraper(url):
    response = requests.get(url, headers=header)
    soup = BeautifulSoup(response.content, 'html.parser')
    dom = et.HTML(str(soup))
    return dom