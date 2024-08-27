from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


chrome_options = webdriver.ChromeOptions()
service = Service(executable_path=ChromeDriverManager().install())
chrome_options.add_argument("--disable-blink-features=AutomationConrtolled")
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                            " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.3")
driver = webdriver.Chrome(service=service, options=chrome_options)
# driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
#     'source': '''
#         delete window.cdc_adoQpoasnfa76pfcZLmcfl_JSON;
#         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Object;
#         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
#         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
#         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
#         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Proxy;
#     '''
# })


def getting_links():
    """   Функция обходит защиту на сайт и парсит ссылки на обявлений
    с 6 страниц и записывает уникальные ссылки в текстовый документ   """
    unique_links = []
    links_urls = []
    URL = ['https://almaty.boplus.kz/uslugi-i-servis/remontnye-i-otdelochnye-raboty/',
           'https://almaty.boplus.kz/uslugi-i-servis/remontnye-i-otdelochnye-raboty/2',
           'https://almaty.boplus.kz/uslugi-i-servis/remontnye-i-otdelochnye-raboty/3',
           'https://almaty.boplus.kz/uslugi-i-servis/remontnye-i-otdelochnye-raboty/4',
           'https://almaty.boplus.kz/uslugi-i-servis/remontnye-i-otdelochnye-raboty/5',
            'https://almaty.boplus.kz/uslugi-i-servis/remontnye-i-otdelochnye-raboty/6']
    for url in URL:
        driver.get(url)
        sleep(3)
        with open('index.html', 'a') as f:
            f.write(driver.page_source)
        with open("index.html") as file:
            src = file.read()
        soup = bs(src, 'lxml')
        links = soup.find_all('a', class_='ad__link')
        for link in links:
            url_card = link.get('href')
            links_urls.append('https:'+url_card)
        for item in links_urls:
            if item not in unique_links:
                unique_links.append(item)
        with open('data_boplus.txt', 'a') as file:
            for item in unique_links:
                file.write(item + '\n')
        print('done')


def main():
    """   Функция парсит данные с сайта boplus.kz
    и записывает их в csv файл   """
    boplus_db = []
    with open('data_boplus.txt', 'r') as file:
        datas = file.read()
    try:
        for url in datas.split('\n'):
            driver.get(url)
            sleep(2)
            soup = bs(driver.page_source, 'lxml')
            phone = soup.find('div', class_='adauthor').find_all('span')[1].text.strip()
            name = soup.find('div', class_='adauthor').find_all('span')[0].text.strip()
            description = soup.find('div', class_='addescription').text.strip()
            boplus_db.append(
                {
                    'phone': phone,
                    'name': name,
                    'description': description
                }
            )
            print('done')
    except Exception as e:
        print(e)
        pass
    df_boplus = pd.DataFrame(boplus_db)
    csv_name = 'data_boplus.csv'
    df_boplus.to_csv(csv_name, index=False)


if __name__ == '__main__':
    # getting_links()
    main()
