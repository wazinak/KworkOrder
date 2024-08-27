from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pandas as pd
from time import sleep


URL = [
    'https://flagma.kz/products/dizayn-interera-i-eksterera/almaty/',
    'https://flagma.kz/products/dizayn-interera-i-eksterera/almaty/page-2/',
    'https://flagma.kz/products/dizayn-interera-i-eksterera/almaty/page-3/',
    'https://flagma.kz/products/dizayn-interera-i-eksterera/almaty/page-4/',
    'https://flagma.kz/products/remontno-stroitelnye-raboty/almaty/',
    'https://flagma.kz/products/remontno-stroitelnye-raboty/almaty/page-2/',
    'https://flagma.kz/products/remontno-stroitelnye-raboty/almaty/page-3/',
    'https://flagma.kz/products/remontno-stroitelnye-raboty/almaty/page-4/',
    'https://flagma.kz/products/remontno-stroitelnye-raboty/almaty/page-5/',
    'https://flagma.kz/products/remontno-stroitelnye-raboty/almaty/page-6/',
    'https://flagma.kz/products/remontno-stroitelnye-raboty/almaty/page-7/',
    'https://flagma.kz/products/remontno-stroitelnye-raboty/almaty/page-8/',
    'https://flagma.kz/products/remontno-stroitelnye-raboty/almaty/page-9/',
    'https://flagma.kz/products/remontno-stroitelnye-raboty/almaty/page-10/',
    'https://flagma.kz/products/remontno-stroitelnye-raboty/almaty/page-11/',
    'https://flagma.kz/products/remontno-stroitelnye-raboty/almaty/page-12/',
    'https://flagma.kz/products/remontno-stroitelnye-raboty/almaty/page-13/',
    'https://flagma.kz/products/remontno-stroitelnye-raboty/almaty/page-14/',
    'https://flagma.kz/products/remontno-stroitelnye-raboty/almaty/page-15/',
    'https://flagma.kz/products/remontno-stroitelnye-raboty/almaty/page-16/',
    'https://flagma.kz/products/remontno-stroitelnye-raboty/almaty/page-17/',
    'https://flagma.kz/products/remontno-stroitelnye-raboty/almaty/page-18/',
    'https://flagma.kz/products/remontno-stroitelnye-raboty/almaty/page-19/',
    'https://flagma.kz/products/remontno-stroitelnye-raboty/almaty/page-20/',
    'https://flagma.kz/products/remontno-stroitelnye-raboty/almaty/page-21/',
    'https://flagma.kz/products/remontno-stroitelnye-raboty/almaty/page-22/',
    'https://flagma.kz/products/remontno-stroitelnye-raboty/almaty/page-23/',
    'https://flagma.kz/products/remontno-stroitelnye-raboty/almaty/page-24/',
    'https://flagma.kz/products/remontno-stroitelnye-raboty/almaty/page-25/',
    'https://flagma.kz/products/remontno-stroitelnye-raboty/almaty/page-26/',
    'https://flagma.kz/products/remontno-stroitelnye-raboty/almaty/page-27/',
    'https://flagma.kz/products/remontno-stroitelnye-raboty/almaty/page-28/',
    'https://flagma.kz/products/remontno-stroitelnye-raboty/almaty/page-29/',
    'https://flagma.kz/products/remontno-stroitelnye-raboty/almaty/page-30/',
    'https://flagma.kz/products/stroitelstvo-i-montazh-inzhenernyh-setey/almaty/',
    'https://flagma.kz/products/stroitelstvo-i-montazh-inzhenernyh-setey/almaty/page-2/',
    'https://flagma.kz/products/stroitelstvo-i-montazh-inzhenernyh-setey/almaty/page-3/',
    'https://flagma.kz/products/otdelochnye-raboty/almaty/',
    'https://flagma.kz/products/otdelochnye-raboty/almaty/page-2/',
    'https://flagma.kz/products/otdelochnye-raboty/almaty/page-3/',
    'https://flagma.kz/products/otdelochnye-raboty/almaty/page-4/',
    'https://flagma.kz/products/otdelochnye-raboty/almaty/page-5/',
]


def get_html():
    links_db = []
    unique_links = []
    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/123.0.0.0 Safari/537.36",
    }
    for url in URL:
        r = requests.get(url=url, headers=headers)
        sleep(1)
        print(r.status_code)
        soup = bs(r.text, 'lxml')
        card_links = soup.find_all('div', class_='page-list-item')
        for toy in card_links:
            try:
                card_link = toy.find('a', class_='photo').get('href')
                print(card_link)
                links_db.append(card_link)
            except Exception:
                pass
        for item in links_db:
            if item not in unique_links:
                unique_links.append(item)
        with open('data_flagma.txt', 'a') as file:
            for item in unique_links:
                file.write(item + '\n')
        print('done')


def main():
    flagma_db = []
    with open('data_flagma.txt', 'r') as f:
        datas = f.read()
        for url in datas.split('\n'):
            try:
                r = requests.get(url)
                print(r.status_code)
                soup = bs(r.text, 'lxml')
                phone = soup.find('div', class_='phones').find('a').text
                name = soup.find('div', class_='user-name').text.strip()
                description = soup.find('div', class_='description').find('p').text.strip()
                print(phone, name, description)
                flagma_db.append(
                    {
                        'phone': phone,
                        'name': name,
                        'description': description
                    }
                )
            except Exception:
                pass
            df_admir = pd.DataFrame(flagma_db)
            csv_name = 'data_flagma.csv'
            df_admir.to_csv(csv_name, index=False)


if __name__ == '__main__':
    # get_html()
    main()