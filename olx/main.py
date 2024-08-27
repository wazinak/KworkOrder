from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pandas as pd
from time import sleep


def olx_parser():
    """  Функция парсинга сайта olx.kz, она находит URL объявлений,
    для того чтобы в дальнейшем парсить уже через Selenium"""

    for i in range(26):
        url = f'https://www.olx.kz/stroitelstvo-remont/?page={i}'
        r = requests.get(url)
        print(r.status_code)
        # with open('index.html', 'w') as f:
        #     f.write(r.text)
        # with open("index.html") as file:
        #     src = file.read()
        unique_data = []
        data = []
        soup = bs(r.text, 'lxml')
        links = soup.find_all(class_='css-z3gu2d')
        for link in links:
            url = link.get('href')
            data.append('https://www.olx.kz' + url)
        for item in data:
            if item not in unique_data:
                unique_data.append(item)
        with open('data_olx.txt', 'a') as file:
            for item in unique_data:
                file.write(item + '\n')
        print('done')


def read_moment():
    """функция парсинга сайта olx.kz уже через Selenium """
    olx_db = []
    chrome_options = webdriver.ChromeOptions()
    service = Service(executable_path=ChromeDriverManager().install())
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1200,900")
    chrome_options.add_argument("--disable-blink-features=AutomationConrtolled")
    # chrome_options.add_argument("--proxy-server=http://127.0.0.1:8888")
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                                " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.3")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    with open('data_olx.txt', 'r') as f:
        datas = f.read()
        for data in datas.split('\n'):
            try:
                driver.get(data)
                print(data)
                sleep(3)
                btn_tel_number = driver.find_element('xpath','//*[@id="mainContent"]/div/div[2]/div[3]/div[2]/div[1]/div/div[5]/div/button[2]')
                # driver.execute_script("arguments[0].scrollIntoView();", btn_tel_number)
                # sleep(3)
                btn_tel_number.click()
                sleep(3)
                soup = bs(driver.page_source, 'lxml')
                try:
                    description = soup.find('div', class_='css-1o924a9').text.strip()
                    phone = soup.find('button', class_='css-1vgbwlu').find('a').text.strip()
                    name = soup.find('div', class_='css-1fp4ipz').find('h4').text.strip()
                    print(phone)
                    olx_db.append(
                        {
                            'phone': phone,
                            'name': name,
                            'description': description,
                        }
                    )
                except Exception as e:
                    print(e)
            except Exception as e:
                pass
    df_olx = pd.DataFrame(olx_db)
    csv_name = 'olx.csv'
    df_olx.to_csv(csv_name)



def check():
    """функция проверки работы селениум"""
    url = 'https://www.olx.kz/d/obyavlenie/krasnyy-kirpich-bystraya-dostavka-s-zavoda-IDoCA4E.html'
    chrome_options = webdriver.ChromeOptions()
    service = Service(executable_path=ChromeDriverManager().install())
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=700,900")
    chrome_options.add_argument("--disable-blink-features=AutomationConrtolled")
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                                " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.3")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url)
    sleep(5)
    knopka = driver.find_element('xpath', '//*[@id="mainContent"]/div/div[2]/div[3]/div[1]/div[2]/div/div[5]/div/button[2]')
    try:
        knopka.click()
    except Exception as e:
        print(f'error {e}')
    sleep(4)
    soup = bs(driver.page_source, 'lxml')
    description = soup.find('div', class_='css-1o924a9').text.strip()
    print(description)
    phone = soup.find('button', class_='css-1vgbwlu').find('a').get('href').replace('tel:', '')
    print(phone)
    name = soup.find('div', class_='css-1fp4ipz').find('h4').text.strip()
    print(name)


def status_url():
    with open('data_olx.txt', 'r') as f:
        datas = f.read()
    for data in datas.split('\n'):
        try:
            r = requests.get(data)
            soup = bs(r.text, 'lxml')
            description = soup.find('div', class_='css-1o924a9').text.strip()
            if description is None:
                print(f'{data} не работает')
        except Exception as e:
            print(f'error {e}')
            pass

if __name__ == '__main__':
    # olx_parser()
    read_moment()
    # check()
    # status_url()
