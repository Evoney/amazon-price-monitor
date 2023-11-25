import pandas as pd
import sys
from service import send_sms, scraper
from utils import get_amazon_price, get_product_name, get_master_price
from extractor import extractor

with open('links.txt') as f:
    links = f.read().splitlines() 

price_drop_products = []
price_drop_list_url = []

dataframe = pd.read_csv('master_data.csv', encoding='unicode_escape')

for product_url in links:
    main_dom = scraper(product_url)
    price = get_amazon_price(main_dom)
    product_name = get_product_name(main_dom)

    if price < get_master_price(product_url, dataframe):
        change_percentage = round((get_master_price(product_url, dataframe) - price) * 100 / get_master_price(product_url, dataframe)) 
        if change_percentage > 10:
            print('There is a {}'.format(change_percentage), '% drop in price for {}'.format(product_name))
            print('Click on link to purchase  {}'.format(product_url))
            price_drop_products.append(product_name)
            price_drop_list_url.append(product_url)

if len(price_drop_products) == 0: 
    sys.exit('No Price drop found')

msg = "There is a drop in price of {}".format(len(price_drop_products)) + " products.\n" + "Click on link to purchase.\n"
for items in price_drop_list_url:
    msg = msg + "\n\n" + items

send_sms(msg)
extractor()
sys.exit('Price drop found')