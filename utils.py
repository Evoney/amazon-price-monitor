def get_amazon_price(dom):
    try:
        price = dom.xpath('//span[@class="a-offscreen"]/text()')[0]
        price = price.replace('.', '').replace('R$', '').replace(',', '.')
        return float(price)
    except Exception as e:
        price = 'Not Available'
        return None

def get_product_name(dom):
    try:
        name = dom.xpath('//span[@id="productTitle"]/text()')
        [name.strip() for name in name]
        return name[0]
    except Exception as e:
        name = 'Not Available'
        return None

def get_master_price(url, df):
    for row in df.itertuples():
        if row.url == url:
            return row.price
    return None