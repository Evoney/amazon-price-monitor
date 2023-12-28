"""Utils module

This is a module to create the utilities functions.
"""
def get_amazon_price(dom):
    """
    Get price.
    """
    try:
        price = dom.xpath('//span[@class="a-offscreen"]/text()')[0]
        price = price.replace('.', '').replace('R$', '').replace(',', '.')
        return float(price)
    except Exception:
        price = 'Not Available'
        return None

def get_product_name(dom):
    """
    Get name.
    """
    try:
        name = dom.xpath('//span[@id="productTitle"]/text()')
        return name[0].strip()
    except Exception:
        name = 'Not Available'
        return None

def get_master_price(url, df):
    """
    Get master price.
    """
    for row in df.itertuples():
        if row.url == url:
            return row.price
    return None
