"""Amazon tracker module

This is a module to create the products prices tracker.
"""
import sys
import pandas as pd
from service import send_sms, scraper
from utils import get_amazon_price, get_product_name, get_master_price
from extractor import extractor

with open('links.txt', encoding="utf-8") as f:
    links = f.read().splitlines()

price_drop_products = []
price_drop_list_url = []
dataframe = pd.read_csv('master_data.csv', encoding='unicode_escape')

for product_url in links:
    main_dom = scraper(product_url)
    price = get_amazon_price(main_dom)
    product_name = get_product_name(main_dom)

    if price < get_master_price(product_url, dataframe):
        master_price = get_master_price(product_url, dataframe)
        change_percentage = round((master_price - price) * 100 / master_price)
        if change_percentage > 10:
            print(f'There is a {change_percentage}',
                  f'% drop in price for {product_name}')
            print(f'Click on link to purchase {product_url}')
            price_drop_products.append(product_name)
            price_drop_list_url.append(product_url)

if len(price_drop_products) == 0:
    sys.exit('No Price drop found')

MSG_ = " products.\n" + "Click on link to purchase.\n"
MSG = f"There is a drop in price of {len(price_drop_products)}" + MSG_  


for items in price_drop_list_url:
    MSG = MSG + "\n\n" + items

send_sms(MSG)
extractor()
sys.exit('Price drop found')
