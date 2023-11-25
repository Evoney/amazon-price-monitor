import time
import random
import csv
from service import scraper
from utils import get_amazon_price, get_product_name

def extractor():
    with open('links.txt') as f:
        links = f.read().splitlines() 

    with open('master_data.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['product name', 'price', 'url'])

        for url in links:
            amazon_dom = scraper(url)

            product_name = get_product_name(amazon_dom)
            product_price = get_amazon_price(amazon_dom)

            time.sleep(random.randint(2, 10))

            writer.writerow([product_name, product_price, url])
            print(product_name, 'price: R$', product_price)

    print('Extract done!')
