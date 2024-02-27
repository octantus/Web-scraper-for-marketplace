import requests
import json


def get_data():
    # получение запроса в cURL
    cookies = {
        '__hash_': '173f440e01214419076f1c8ef369c86b',
        '__lhash_': 'dea9188bb2e35d30da084f2715b4e5b1',
        'MVID_ENVCLOUD': 'prod2',
        'MVID_AB_PERSONAL_RECOMMENDS': 'true',
        'MVID_AB_UPSALE': 'true',
        'MVID_ACCESSORIES_PDP_BY_RANK': 'true',
        'MVID_ALFA_PODELI_NEW': 'true',
        'MVID_CASCADE_CMN': 'true',
        'MVID_CATALOG_NEW': 'true',
        'MVID_CHAT_VERSION': '6.6.0',
        'MVID_CITY_ID': 'CityCZ_975',
        'MVID_CREDIT_DIGITAL': 'true',
        'MVID_CREDIT_SERVICES': 'true',
        'MVID_CRITICAL_GTM_INIT_DELAY': '3000',
        'MVID_DISPLAY_ACCRUED_BR': 'true',
        'MVID_DISPLAY_PERS_DISCOUNT': '2',
        'MVID_EMPLOYEE_DISCOUNT': 'true',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GEOLOCATION_NEEDED': 'true',
        'MVID_GTM_ENABLED': '011',
        'MVID_INTERVAL_DELIVERY': 'true',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_KLADR_ID': '7700000000000',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_NEW_CHAT_PDP': 'true',
        'MVID_NEW_GET_SHOPPING_CART_HIT_PRODUCTS': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_NEW_POST_SHOPPING_CART_AUTHORIZE': 'true',
        'MVID_NEW_POST_SHOPPING_CART_USEFUL_PRODUCTS': 'true',
        'MVID_PODELI_PDP': 'true',
        'MVID_PROMO_PAGES_ON_2': 'true',
        'MVID_REGION_ID': '1',
        'MVID_REGION_SHOP': 'S002',
        'MVID_SERVICES': '111',
        'MVID_SERVICE_AVLB': 'true',
        'MVID_SINGLE_CHECKOUT': 'true',
        'MVID_SP': 'true',
        'MVID_TIMEZONE_OFFSET': '3',
        'MVID_TYP_CHAT': 'true',
        'MVID_WEB_SBP': 'true',
        'SENTRY_ERRORS_RATE': '0.1',
        'SENTRY_TRANSACTIONS_RATE': '0.5',
        'mindboxDeviceUUID': 'ff08d397-22fa-4f72-8995-972d83579718',
        'directCrm-session': '%7B%22deviceGuid%22%3A%22ff08d397-22fa-4f72-8995-972d83579718%22%7D',
        '_ym_uid': '1708979602229232936',
        '_ym_d': '1708979602',
        '_sp_ses.d61c': '*',
        '_ym_isad': '1',
        '_ym_visorc': 'w',
        '_ga': 'GA1.1.799704625.1708979602',
        '__SourceTracker': 'google__organic',
        'admitad_deduplication_cookie': 'google__organic',
        'SMSError': '',
        'authError': '',
        'gdeslon.ru.__arc_domain': 'gdeslon.ru',
        'gdeslon.ru.user_id': '981a4666-041b-49d0-a231-77926d6660ea',
        'tmr_lvid': '1fdeb4d72233ec71e780fdbe1d380843',
        'tmr_lvidTS': '1708979605194',
        'flocktory-uuid': 'c1936815-33b5-4118-bd53-994b43217110-7',
        'customer_email': 'null',
        'uxs_uid': '4a86d120-d4e6-11ee-b74b-bbbc261538f1',
        'advcake_track_id': '4d629f18-ea5f-835d-4757-6272d6d89e76',
        'advcake_session_id': 'c3c40166-98f4-6286-9b47-9a7ded1cba0f',
        '_gpVisits': '{"isFirstVisitDomain":true,"idContainer":"100025D5"}',
        'flacktory': 'no',
        'BIGipServeratg-ps-prod_tcp80': '1912921098.20480.0000',
        'bIPs': '155255760',
        'afUserId': '3c0f93c4-a80e-4058-8bc5-d34a272087b2-p',
        'AF_SYNC': '1708979612473',
        'adid': '170897961248006',
        'gsscgib-w-mvideo': 'aCWP18rlCxxw4OsJXC5rVMfFP9T31MFjeKcxqCAxcVTbzCb3BTtsOr9mD0l5ASfwCCyq0lJeNVFGkqd9gDviebC1caS0u05AP8HC/M3izENvzgXpG/8fob7GWY1vWsSgQM6ifxxLsRi0QSWOXb5OhfPslgmHedI1FwXlSFEYU/I9GF1F85geuAoT3rrHqtPArds78aEn3hrZxIZvyx/wT9UeLud5GUQX79y5JkAB8vCvnPZ9ZcgHDXLXeInpTg==',
        'gsscgib-w-mvideo': 'aCWP18rlCxxw4OsJXC5rVMfFP9T31MFjeKcxqCAxcVTbzCb3BTtsOr9mD0l5ASfwCCyq0lJeNVFGkqd9gDviebC1caS0u05AP8HC/M3izENvzgXpG/8fob7GWY1vWsSgQM6ifxxLsRi0QSWOXb5OhfPslgmHedI1FwXlSFEYU/I9GF1F85geuAoT3rrHqtPArds78aEn3hrZxIZvyx/wT9UeLud5GUQX79y5JkAB8vCvnPZ9ZcgHDXLXeInpTg==',
        'tmr_detect': '1%7C1708980103060',
        '_gp100025D5': '{"hits":3,"vc":1,"ac":1,"a6":1}',
        '_sp_id.d61c': '36e16c3e-4c19-4794-b4e2-a6a9cf18b5a5.1708979602.1.1708980115..f0a546ea-bac8-47ed-90db-5f1e955ea288..817f3559-0d09-46c5-b374-30abd66e76ab.1708979601706.53',
        'fgsscgib-w-mvideo': 'Qk8B7f4171a53b7fe5ae0e7119f47eadcbaebbfb',
        'fgsscgib-w-mvideo': 'Qk8B7f4171a53b7fe5ae0e7119f47eadcbaebbfb',
        'gsscgib-w-mvideo': 'FWBWUgDNVn48QwteIrSMoGpoaBRtCr0cZ0WZt3m1cIVjwBoB1SfDX6IDu6TkwZUZ9dYeCnAh4t/3bIaYRHkCptr5chFV06++PWG0lFnX8v9y/QkR0xwO2B+bNLJyKwIFbu0uRzxfl7aqVFBhpwvVqhAd8Mp5qwjazMxXCbV/R6a1rS9A6iYE2oKe8qu5ZFkoz1Q5uXRcEjjhEBCDz0P2udlMf4a40XpSKcKZFYuVNgQFHxO/T50ZhmuD9XoHQQ==',
        'cfidsgib-w-mvideo': 'Kw1+N2D+FDAzaGqbNfphAK3t1Uuwww0FEigYuwBJXkkgbny1YSNMozkaswrEnpfvz+SO8+n45KaJ+CSLyx8z9ONojubM1dLvWNvKmbvDCjEKAQ+BLKAx3miTBcU+qQ6wxgriJtEAeZCPv2numzSCQIM/pAdvWiXOYk32zQ==',
        '_ga_CFMZTSS5FM': 'GS1.1.1708979601.1.1.1708980119.0.0.0',
        '_ga_BNX5WPP3YK': 'GS1.1.1708979601.1.1.1708980119.37.0.0',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,ru;q=0.7',
        'baggage': 'sentry-environment=production,sentry-release=release_24_2_4(6000),sentry-public_key=ae7d267743424249bfeeaa2e347f4260,sentry-trace_id=7ddcb52643d243929bc8b527ef144c9b,sentry-sample_rate=0.5,sentry-transaction=%2F**%2F,sentry-sampled=false',
        # 'cookie': '__hash_=173f440e01214419076f1c8ef369c86b; __lhash_=dea9188bb2e35d30da084f2715b4e5b1; MVID_ENVCLOUD=prod2; MVID_AB_PERSONAL_RECOMMENDS=true; MVID_AB_UPSALE=true; MVID_ACCESSORIES_PDP_BY_RANK=true; MVID_ALFA_PODELI_NEW=true; MVID_CASCADE_CMN=true; MVID_CATALOG_NEW=true; MVID_CHAT_VERSION=6.6.0; MVID_CITY_ID=CityCZ_975; MVID_CREDIT_DIGITAL=true; MVID_CREDIT_SERVICES=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_DISPLAY_ACCRUED_BR=true; MVID_DISPLAY_PERS_DISCOUNT=2; MVID_EMPLOYEE_DISCOUNT=true; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GTM_ENABLED=011; MVID_INTERVAL_DELIVERY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=7700000000000; MVID_LAYOUT_TYPE=1; MVID_NEW_CHAT_PDP=true; MVID_NEW_GET_SHOPPING_CART_HIT_PRODUCTS=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_NEW_POST_SHOPPING_CART_AUTHORIZE=true; MVID_NEW_POST_SHOPPING_CART_USEFUL_PRODUCTS=true; MVID_PODELI_PDP=true; MVID_PROMO_PAGES_ON_2=true; MVID_REGION_ID=1; MVID_REGION_SHOP=S002; MVID_SERVICES=111; MVID_SERVICE_AVLB=true; MVID_SINGLE_CHECKOUT=true; MVID_SP=true; MVID_TIMEZONE_OFFSET=3; MVID_TYP_CHAT=true; MVID_WEB_SBP=true; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; mindboxDeviceUUID=ff08d397-22fa-4f72-8995-972d83579718; directCrm-session=%7B%22deviceGuid%22%3A%22ff08d397-22fa-4f72-8995-972d83579718%22%7D; _ym_uid=1708979602229232936; _ym_d=1708979602; _sp_ses.d61c=*; _ym_isad=1; _ym_visorc=w; _ga=GA1.1.799704625.1708979602; __SourceTracker=google__organic; admitad_deduplication_cookie=google__organic; SMSError=; authError=; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=981a4666-041b-49d0-a231-77926d6660ea; tmr_lvid=1fdeb4d72233ec71e780fdbe1d380843; tmr_lvidTS=1708979605194; flocktory-uuid=c1936815-33b5-4118-bd53-994b43217110-7; customer_email=null; uxs_uid=4a86d120-d4e6-11ee-b74b-bbbc261538f1; advcake_track_id=4d629f18-ea5f-835d-4757-6272d6d89e76; advcake_session_id=c3c40166-98f4-6286-9b47-9a7ded1cba0f; _gpVisits={"isFirstVisitDomain":true,"idContainer":"100025D5"}; flacktory=no; BIGipServeratg-ps-prod_tcp80=1912921098.20480.0000; bIPs=155255760; afUserId=3c0f93c4-a80e-4058-8bc5-d34a272087b2-p; AF_SYNC=1708979612473; adid=170897961248006; gsscgib-w-mvideo=aCWP18rlCxxw4OsJXC5rVMfFP9T31MFjeKcxqCAxcVTbzCb3BTtsOr9mD0l5ASfwCCyq0lJeNVFGkqd9gDviebC1caS0u05AP8HC/M3izENvzgXpG/8fob7GWY1vWsSgQM6ifxxLsRi0QSWOXb5OhfPslgmHedI1FwXlSFEYU/I9GF1F85geuAoT3rrHqtPArds78aEn3hrZxIZvyx/wT9UeLud5GUQX79y5JkAB8vCvnPZ9ZcgHDXLXeInpTg==; gsscgib-w-mvideo=aCWP18rlCxxw4OsJXC5rVMfFP9T31MFjeKcxqCAxcVTbzCb3BTtsOr9mD0l5ASfwCCyq0lJeNVFGkqd9gDviebC1caS0u05AP8HC/M3izENvzgXpG/8fob7GWY1vWsSgQM6ifxxLsRi0QSWOXb5OhfPslgmHedI1FwXlSFEYU/I9GF1F85geuAoT3rrHqtPArds78aEn3hrZxIZvyx/wT9UeLud5GUQX79y5JkAB8vCvnPZ9ZcgHDXLXeInpTg==; tmr_detect=1%7C1708980103060; _gp100025D5={"hits":3,"vc":1,"ac":1,"a6":1}; _sp_id.d61c=36e16c3e-4c19-4794-b4e2-a6a9cf18b5a5.1708979602.1.1708980115..f0a546ea-bac8-47ed-90db-5f1e955ea288..817f3559-0d09-46c5-b374-30abd66e76ab.1708979601706.53; fgsscgib-w-mvideo=Qk8B7f4171a53b7fe5ae0e7119f47eadcbaebbfb; fgsscgib-w-mvideo=Qk8B7f4171a53b7fe5ae0e7119f47eadcbaebbfb; gsscgib-w-mvideo=FWBWUgDNVn48QwteIrSMoGpoaBRtCr0cZ0WZt3m1cIVjwBoB1SfDX6IDu6TkwZUZ9dYeCnAh4t/3bIaYRHkCptr5chFV06++PWG0lFnX8v9y/QkR0xwO2B+bNLJyKwIFbu0uRzxfl7aqVFBhpwvVqhAd8Mp5qwjazMxXCbV/R6a1rS9A6iYE2oKe8qu5ZFkoz1Q5uXRcEjjhEBCDz0P2udlMf4a40XpSKcKZFYuVNgQFHxO/T50ZhmuD9XoHQQ==; cfidsgib-w-mvideo=Kw1+N2D+FDAzaGqbNfphAK3t1Uuwww0FEigYuwBJXkkgbny1YSNMozkaswrEnpfvz+SO8+n45KaJ+CSLyx8z9ONojubM1dLvWNvKmbvDCjEKAQ+BLKAx3miTBcU+qQ6wxgriJtEAeZCPv2numzSCQIM/pAdvWiXOYk32zQ==; _ga_CFMZTSS5FM=GS1.1.1708979601.1.1.1708980119.0.0.0; _ga_BNX5WPP3YK=GS1.1.1708979601.1.1.1708980119.37.0.0',
        'priority': 'u=1, i',
        'referer': 'https://www.mvideo.ru/noutbuki-planshety-komputery-8/noutbuki-118?f_tolko-v-nalichii=da&f_skidka=da',
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sentry-trace': '7ddcb52643d243929bc8b527ef144c9b-8022847d7b9f0c44-0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'x-set-application-id': 'f4592726-eec1-49b3-bd1a-10a14fd4eddf',
    }
    # параметры
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
    # запросили данные и, так как все данные лежат по разным запросам, будем получать каждый
    response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies, headers=headers).json()
   
    # собираем айдишники ноутбуков
    laptop_ids = response.get('body').get('products') # лежат в body -> products
    with open('laptop_ids.json', 'w') as file:
        json.dump(laptop_ids, file, indent=4, ensure_ascii='False')

    # сбор подробной информации о ноутбуках: название/модель/характеристики и т.д.
    json_data = {
        'productIds': laptop_ids,
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
    
    response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers, json=json_data).json()
    with open('laptops.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii='False')

    # cбор данных о ценах/бонусах за покупку ноутбуков
    laptop_ids_string = ','.join(laptop_ids) # айдишники в запросе в виде строки, а у нас список

    params = {
        'productIds': laptop_ids_string,
        'addBonusRubles': 'true',
        'isPromoApplied': 'true',
    }
    response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies, headers=headers).json()
    with open('laptop_prices.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii='False')

    all_laptops_price = {}

    price_info = response.get('body').get('materialPrices')
    for item in price_info:
        lap_id = item.get('price').get('productId')
        base_price = item.get('price').get('basePrice')
        sale_price = item.get('price').get('salePrice')
        bonuses = item.get('bonusRubles').get('total')
        #discount_sale = item.get('price').get('discounts')
        all_laptops_price[lap_id] = {
            'base_price' : base_price,
            'sale_price' : sale_price,
            'bonuses' : bonuses#,
           # 'discount' : discount_sale
        }

    with open('lap_prices_bonuses.json', 'w') as file:
        json.dump(all_laptops_price, file, indent=4, ensure_ascii='False')

def get_all_info():
    with open('laptops.json') as file:
        laptops_data = json.load(file)
    with open('lap_prices_bonuses.json') as file:
        laptops_cost = json.load(file)

    laptops_data = laptops_data.get('body').get('products')
    for item in laptops_data:
        lap_id = item.get('productId')
        if lap_id in laptops_cost:
            final_prices = laptops_cost[lap_id]

        item['base_price'] = final_prices.get('base_price')
        item['sale_price'] = final_prices.get('sale_price')
        item['bonuses'] = final_prices.get('bonuses')
    with open('total_result.json', 'w') as file:
        json.dump(laptops_data, file, indent=4, ensure_ascii=False)


def main():
    get_data()
    get_all_info()

if __name__ == '__main__':
    main()