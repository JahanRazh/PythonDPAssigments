import requests
import json
import sys
sys.path.insert(0,'bs4.zip')
from bs4 import BeautifulSoup

#Imitate the Mozilla browser.
user_agent = {'User-agent': 'Mozilla/5.0'}

def compare_prices(product_laughs, product_glomark):
    # Acquire web pages
    laughs_page = requests.get(product_laughs, headers=user_agent)
    glomark_page = requests.get(product_glomark, headers=user_agent)

    # Parse Laughs page
    laughs_soup = BeautifulSoup(laughs_page.content, 'html.parser')
    
    # Get Laughs price - looking specifically for the special price span
    price_elem = laughs_soup.select_one('span.special-price span.price')
    if not price_elem:
        price_elem = laughs_soup.select_one('span.regular-price')
    if price_elem:
        price_text = price_elem.get_text().strip().replace('Rs.', '').replace(',', '')
        price_laughs = float(price_text)
    
    # Get Laughs product name
    name_elem = laughs_soup.select_one('div.product-name')
    if name_elem:
        product_name_laughs = name_elem.get_text().strip()
    else:
        product_name_laughs = "Unknown Product"

    # Parse Glomark page
    glomark_soup = BeautifulSoup(glomark_page.content, 'html.parser')
    
    # Find all script tags and look for the one containing product data
    script_tags = glomark_soup.find_all('script', type='application/ld+json')
    price_glomark = None
    product_name_glomark = None
    
    for script in script_tags:
        try:
            json_data = json.loads(script.string)
            # Handle case where json_data is a list
            if isinstance(json_data, list):
                for item in json_data:
                    if isinstance(item, dict) and 'offers' in item:
                        if isinstance(item['offers'], dict):
                            price_glomark = float(item['offers']['price'])
                        else:
                            price_glomark = float(item['offers'][0]['price'])
                        product_name_glomark = item.get('name', 'Unknown Product')
                        break
            # Handle case where json_data is a dict
            elif isinstance(json_data, dict) and 'offers' in json_data:
                if isinstance(json_data['offers'], dict):
                    price_glomark = float(json_data['offers']['price'])
                else:
                    price_glomark = float(json_data['offers'][0]['price'])
                product_name_glomark = json_data.get('name', 'Unknown Product')
                break
        except (json.JSONDecodeError, KeyError, ValueError, TypeError):
            continue

    # Print results
    print('Laughs  ', product_name_laughs, 'Rs.: ', price_laughs)
    print('Glomark ', product_name_glomark, 'Rs.: ', price_glomark)
    
    if(price_laughs > price_glomark):
        print('Glomark is cheaper Rs.:', price_laughs - price_glomark)
    elif(price_laughs < price_glomark):
        print('Laughs is cheaper Rs.:', price_glomark - price_laughs)    
    else:
        print('Price is the same')
