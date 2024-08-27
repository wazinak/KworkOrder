from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pandas as pd
from time import sleep


URL = [
    'https://almaty.salexy.kz/rabota/ishu_rabotu/arhitektura_i_stroitelstvo/arhitektory?Filter%5Bsearch_string%5D=%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D1%81%D1%82%D0%B2%D0%BE&Filter%5Bprice%5D%5Bmin%5D=&Filter%5Bprice%5D%5Bmax%5D=&Filter%5Bsort_by%5D=',
    'https://almaty.salexy.kz/rabota/ishu_rabotu/arhitektura_i_stroitelstvo/proraby_brigadiry_mastera',
    'https://almaty.salexy.kz/rabota/ishu_rabotu/arhitektura_i_stroitelstvo/rabochie_stroitelnyh_specialnostey',
    'https://almaty.salexy.kz/rabota/ishu_rabotu/arhitektura_i_stroitelstvo/rabochie_stroitelnyh_specialnostey?page=2',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/remont_kvartir',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/remont_kvartir?page=2',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/remont_kvartir?page=3',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/remont_kvartir?page=4',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/remont_kvartir?page=5',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/remont_kvartir?page=6',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/remont_kvartir?page=7',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/remont_kvartir?page=8',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/remont_kvartir?page=9',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/remont_kvartir?page=10',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/remont_kvartir?page=11',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/remont_kvartir?page=12',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/remont_kvartir?page=13',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/remont_kvartir?page=14',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/remont_kvartir?page=15',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/remont_kvartir?page=16',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/remont_kvartir?page=17',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/remont_kvartir?page=18',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/remont_kvartir?page=19',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/remont_kvartir?page=20',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/remont_kvartir?page=21',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/remont_kvartir?page=22',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/remont_kvartir?page=23',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/remont_kvartir?page=24',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/remont_kvartir?page=25',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/remont_kvartir?page=26',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/remont_kvartir?page=27',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/remont_kvartir?page=28',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/remont_kvartir?page=29',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/remont_kvartir?page=30',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/remont_kvartir?page=31',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/remont_kvartir?page=32',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/remont_kvartir?page=33',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/remont_kvartir?page=34',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/remont_kvartir?page=35',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/remont_kvartir?page=36',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/remont_kvartir?page=37',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/remont_kvartir?page=38',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/remont_kvartir?page=39',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/remont_kvartir?page=40',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/stroitelnie_uslugi',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/stroitelnie_uslugi?page=2',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/stroitelnie_uslugi?page=3',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/stroitelnie_uslugi?page=4',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/stroitelnie_uslugi?page=5',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/stroitelnie_uslugi?page=6',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/stroitelnie_uslugi?page=7',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/stroitelnie_uslugi?page=8',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/stroitelnie_uslugi?page=9',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/stroitelnie_uslugi?page=10',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/stroitelnie_uslugi?page=11',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/stroitelnie_uslugi?page=12',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/stroitelnie_uslugi?page=13',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/stroitelnie_uslugi?page=14',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/stroitelnie_uslugi?page=15',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/stroitelnie_uslugi?page=16',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/stroitelnie_uslugi?page=17',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/stroitelnie_uslugi?page=18',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/stroitelnie_uslugi?page=19',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/stroitelnie_uslugi?page=20',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/stroitelnie_uslugi?page=21',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/stroitelnie_uslugi?page=22',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/stroitelnie_uslugi?page=23',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/stroitelnie_uslugi?page=24',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/stroitelnie_uslugi?page=25',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/stroitelnie_uslugi?page=26',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/stroitelnie_uslugi?page=27',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/stroitelnie_uslugi?page=28',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/stroitelnie_uslugi?page=29',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/stroitelnie_uslugi?page=30',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/stroitelnie_uslugi?page=31',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/stroitelnie_uslugi?page=32',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/stroitelnie_uslugi?page=33',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/stroitelnie_uslugi?page=34',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/stroitelnie_uslugi?page=35',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/stroitelnie_uslugi?page=36',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/stroitelnie_uslugi?page=37',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/stroitelnie_uslugi?page=38',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/stroitelnie_uslugi?page=39',
    'https://almaty.salexy.kz/remont_i_stroitelstvo/stroitelnie_uslugi?page=40',
]


def get_html():
    links_db = []
    unique_links = []
    for url in URL:
        r = requests.get(url)
        print(r.status_code)
        soup = bs(r.text, 'lxml')
        card_links = soup.find_all('div', class_='title')
        for toy in card_links:
            card_link = toy.find('a').get('href')
            links_db.append(card_link)
        for item in links_db:
            if item not in unique_links:
                unique_links.append(item)
        with open('data_salexy.txt', 'a') as file:
            for item in unique_links:
                file.write(item + '\n')
        print('done')

def main():
    salexy_db = []
    url = 'https://astana.salexy.kz/c/gotovlyu_tendera_po_stroitelstvu_na_platforme_elektronnyh_goszakupok_5139758.html'
    chrome_options = webdriver.ChromeOptions()
    service = Service(executable_path=ChromeDriverManager().install())
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=7"
                                "00,900")
    # chrome_options.add_argument("--disable-blink-features=AutomationConrtolled")
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                                " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.3")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    with open('data_salexy.txt', 'r') as file:
        datas = file.read()
        for data in datas.split('\n'):
            try:
                driver.get(data)
                sleep(4)
                btn = driver.find_element('xpath', '/html/body/div[1]/div/div/div[2]/div/div[4]/div/div[2]/div[1]/div[1]/div[1]')
                driver.execute_script("arguments[0].scrollIntoView();", btn)
                sleep(2)
                print(data)
                btn.click()
                sleep(5)
                soup = bs(driver.page_source, 'lxml')
                sleep(2)
                try:
                    phone = soup.find('div', class_='btn-holder tel-item').find('a').text.strip()
                    sleep(1)
                    print(phone)
                    name = soup.find('div', class_='title').find('a').text.strip()
                    description = soup.find('div', class_='description').find('p').text.strip()
                    salexy_db.append(
                        {
                            'phone': phone,
                            'name': name,
                            'description': description,
                        }
                    )
                except Exception as e:
                    print(e)
            except Exception as e:
                continue
        df_olx = pd.DataFrame(salexy_db)
        csv_name = 'salexy.csv'
        df_olx.to_csv(csv_name)


def del_duplicate():
    with open('data_salexy.txt', 'r') as file:
        lines = file.readlines()

    unique_lines = list(set(lines))

    with open('data_salexy.txt', 'w') as file:
        file.writelines(unique_lines)


if __name__ == '__main__':
    # get_html()
    main()
    # del_duplicate()
