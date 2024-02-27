from configuration import headers, cookies
import requests
import json
import os
import math


def get_data():
    # получение запроса в cURL
    params = {
        'categoryId': '118',
        'offset': '0',
        'limit': '24',
        'filterParams': [
            'WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==',
            'WyJza2lka2EiLCIiLCJkYSJd',
        ],
        'doTranslit': 'true',
    }

    if not os.path.exists('data'): # создаем директорию под data
        os.mkdir('data')

    s = requests.Session() # создаем сессию
    # запросили данные и, так как все данные лежат по разным запросам, будем получать каждый
    response = s.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies, headers=headers).json()
    
    items_count = response.get('body').get('total') # для пагинации получим количество товаров на странице
    
    if items_count is None:
        return '[!] None'
    
    pages_count = math.ceil(items_count / 24)
   
    item_ids = {}
    item_description = {}
    item_prices = {}

    for i in range(pages_count):
        offset = f'{i * 24}'

        params = {
            'categoryId': '118',
            'offset': offset,
            'limit': '24',
            'filterParams': [
                'WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==',
                'WyJza2lka2EiLCIiLCJkYSJd',
            ],
            'doTranslit': 'true',
        }

        response = s.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies, headers=headers).json()
        laptop_ids_list = response.get('body').get('products') # лежат в body -> products
        item_ids[i] = laptop_ids_list # сбор id
        
        json_data = { # сбор подробной информации о ноутбуках: название/модель/характеристики и т.д.
            'productIds': laptop_ids_list,
            'mediaTypes': [
                'images',
            ],
            'category': True,
            'status': True,
            'brand': True,
            'propertyTypes': [
                'KEY',
            ],
            'propertiesConfig': {
                'propertiesPortionSize': 5,
            },
            'multioffer': False,
        }
        response = s.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers, json=json_data).json()
        item_description[i] = response
        
        laptop_ids_string = ','.join(laptop_ids_list) # айдишники в запросе в виде строки, а у нас список

        params = { # cбор данных о ценах/бонусах за покупку ноутбуков
            'productIds': laptop_ids_string,
            'addBonusRubles': 'true',
            'isPromoApplied': 'true',
        }

        response = s.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies, headers=headers).json()
        material_prices = response.get('body').get('materialPrices')
        
        for item in material_prices:
            lap_id = item.get('price').get('productId')
            base_price = item.get('price').get('basePrice')
            sale_price = item.get('price').get('salePrice')
            bonuses = item.get('bonusRubles').get('total')
            #discount_sale = item.get('price').get('discounts') - возможность достать значение скидки
            
            item_prices[lap_id] = {
                'base_price' : base_price,
                'sale_price' : sale_price,
                'bonuses' : bonuses
            # 'discount' : discount_sale
            }
        print(f'[+] Completed {i + 1} of the {pages_count} pages')

# запись данных
    with open('data/item_ids_1.json', 'w') as file:
        json.dump(item_ids, file, indent=4, ensure_ascii='False')
    with open('data/item_description_2.json', 'w') as file:
        json.dump(item_description, file, indent=4, ensure_ascii='False')
    with open('data/item_prices_3.json', 'w') as file:
        json.dump(item_prices, file, indent=4, ensure_ascii='False')

def get_all_info():
    with open('data/item_description_2.json') as file:
        laptops_data = json.load(file)
    with open('data/item_prices_3.json') as file:
        laptops_cost = json.load(file)
 
    for items in laptops_data.values():
        products = items.get('body').get('products')
        for item in products:
            lap_id = item.get('productId')
            if lap_id in laptops_cost:
                final_prices = laptops_cost[lap_id]
            item['base_price'] = final_prices.get('base_price')
            item['sale_price'] = final_prices.get('sale_price')
            item['bonuses'] = final_prices.get('bonuses')
            item['item'] = f'https://www.mvideo.ru/products/{item.get("nameTranslit")}-{lap_id}'
    with open('data/total_result_4.json', 'w') as file:
        json.dump(laptops_data, file, indent=4, ensure_ascii=False)


def main():
    get_data()
    get_all_info()

if __name__ == '__main__':
    main()
