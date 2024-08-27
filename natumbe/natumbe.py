from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pandas as pd
from time import sleep


URL = [
    'https://natumbe.kz/almaty/izgotovlenije-mebeli-na-zakaz/',
    'https://natumbe.kz/almaty/izgotovlenije-mebeli-na-zakaz/?c=3100&lt=gallery&page=2',
    'https://natumbe.kz/almaty/izgotovlenije-mebeli-na-zakaz/?c=3100&lt=gallery&page=3',
    'https://natumbe.kz/almaty/izgotovlenije-mebeli-na-zakaz/?c=3100&lt=gallery&page=4',
    'https://natumbe.kz/almaty/izgotovlenije-mebeli-na-zakaz/?c=3100&lt=gallery&page=5',
    'https://natumbe.kz/almaty/izgotovlenije-mebeli-na-zakaz/?c=3100&lt=gallery&page=6',
    'https://natumbe.kz/almaty/izgotovlenije-mebeli-na-zakaz/?c=3100&lt=gallery&page=7',
    'https://natumbe.kz/almaty/izgotovlenije-mebeli-na-zakaz/?c=3100&lt=gallery&page=8',
    'https://natumbe.kz/almaty/izgotovlenije-mebeli-na-zakaz/?c=3100&lt=gallery&page=9',
    'https://natumbe.kz/almaty/izgotovlenije-mebeli-na-zakaz/?c=3100&lt=gallery&page=10',
    'https://natumbe.kz/almaty/izgotovlenije-mebeli-na-zakaz/?c=3100&lt=gallery&page=11',
    'https://natumbe.kz/almaty/ukladka-plitki/',
    'https://natumbe.kz/almaty/ukladka-plitki/?c=3092&lt=gallery&page=2',
    'https://natumbe.kz/almaty/ukladka-plitki/?c=3092&lt=gallery&page=3',
    'https://natumbe.kz/almaty/ukladka-plitki/?c=3092&lt=gallery&page=4',
    'https://natumbe.kz/almaty/ukladka-plitki/?c=3092&lt=gallery&page=5',
    'https://natumbe.kz/almaty/ukladka-plitki/?c=3092&lt=gallery&page=6',
    'https://natumbe.kz/almaty/ukladka-plitki/?c=3092&lt=gallery&page=7',
    'https://natumbe.kz/almaty/montazhnyje-raboty/',
    'https://natumbe.kz/almaty/montazhnyje-raboty/?c=3024&lt=gallery&page=2',
    'https://natumbe.kz/almaty/montazhnyje-raboty/?c=3024&lt=gallery&page=3',
    'https://natumbe.kz/almaty/montazhnyje-raboty/?c=3024&lt=gallery&page=4',
    'https://natumbe.kz/almaty/gipsokartonnyje-raboty/',
    'https://natumbe.kz/almaty/stolarnyje-raboty/',
    'https://natumbe.kz/almaty/stolarnyje-raboty/?c=3099&lt=gallery&page=2',
    'https://natumbe.kz/almaty/stolarnyje-raboty/?c=3099&lt=gallery&page=3',
    'https://natumbe.kz/almaty/uslugi-svarshhika/',
    'https://natumbe.kz/almaty/uslugi-svarshhika/?c=3091&lt=gallery&page=2',
    'https://natumbe.kz/almaty/uslugi-svarshhika/?c=3091&lt=gallery&page=3',
    'https://natumbe.kz/almaty/uslugi-svarshhika/?c=3091&lt=gallery&page=4',
    'https://natumbe.kz/almaty/uslugi-svarshhika/?c=3091&lt=gallery&page=5',
    'https://natumbe.kz/almaty/uslugi-svarshhika/?c=3091&lt=gallery&page=6',
    'https://natumbe.kz/almaty/uslugi-svarshhika/?c=3091&lt=gallery&page=7',
    'https://natumbe.kz/almaty/uslugi-svarshhika/?c=3091&lt=gallery&page=8',
    'https://natumbe.kz/almaty/uslugi-svarshhika/?c=3091&lt=gallery&page=9',
    'https://natumbe.kz/almaty/uslugi-svarshhika/?c=3091&lt=gallery&page=10',
    'https://natumbe.kz/almaty/uslugi/stroitelstvo-otdelka-remont/remont-kvartiry/',
    'https://natumbe.kz/almaty/stroitelnyje-uslugi/',
    'https://natumbe.kz/almaty/stroitelnyje-uslugi/?c=3023&lt=gallery&page=2',
    'https://natumbe.kz/almaty/stroitelnyje-uslugi/?c=3023&lt=gallery&page=3',
    'https://natumbe.kz/almaty/stroitelnyje-uslugi/?c=3023&lt=gallery&page=4',
    'https://natumbe.kz/almaty/stroitelnyje-uslugi/?c=3023&lt=gallery&page=5',
    'https://natumbe.kz/almaty/stroitelnyje-uslugi/?c=3023&lt=gallery&page=6',
    'https://natumbe.kz/almaty/stroitelnyje-uslugi/?c=3023&lt=gallery&page=7',
    'https://natumbe.kz/almaty/stroitelnyje-uslugi/?c=3023&lt=gallery&page=8',
    'https://natumbe.kz/almaty/stroitelnyje-uslugi/?c=3023&lt=gallery&page=9',
    'https://natumbe.kz/almaty/stroitelnyje-uslugi/?c=3023&lt=gallery&page=10',
    'https://natumbe.kz/almaty/elektrika/',
    'https://natumbe.kz/almaty/elektrika/?c=828&lt=gallery&page=2',
    'https://natumbe.kz/almaty/elektrika/?c=828&lt=gallery&page=3',
    'https://natumbe.kz/almaty/elektrika/?c=828&lt=gallery&page=4',
    'https://natumbe.kz/almaty/elektrika/?c=828&lt=gallery&page=5',
    'https://natumbe.kz/almaty/elektrika/?c=828&lt=gallery&page=6',
    'https://natumbe.kz/almaty/remont-vannoj/',
    'https://natumbe.kz/almaty/stroitelnye-uslugi/',
    'https://natumbe.kz/almaty/napolnyje-raboty/',
    'https://natumbe.kz/almaty/napolnyje-raboty/?c=3095&lt=gallery&page=2',
    'https://natumbe.kz/almaty/malarnyje-raboty/',
    'https://natumbe.kz/almaty/malarnyje-raboty/?c=3097&lt=gallery&page=2',
    'https://natumbe.kz/almaty/malarnyje-raboty/?c=3097&lt=gallery&page=3',
    'https://natumbe.kz/almaty/malarnyje-raboty/?c=3097&lt=gallery&page=4',
    'https://natumbe.kz/almaty/malarnyje-raboty/?c=3097&lt=gallery&page=5',
    'https://natumbe.kz/almaty/malarnyje-raboty/?c=3097&lt=gallery&page=6',
    'https://natumbe.kz/almaty/malarnyje-raboty/?c=3097&lt=gallery&page=7',
    'https://natumbe.kz/almaty/malarnyje-raboty/?c=3097&lt=gallery&page=8',
    'https://natumbe.kz/almaty/malarnyje-raboty/?c=3097&lt=gallery&page=9',
    'https://natumbe.kz/almaty/malarnyje-raboty/?c=3097&lt=gallery&page=10',
    'https://natumbe.kz/almaty/malarnyje-raboty/?c=3097&lt=gallery&page=11',
    'https://natumbe.kz/almaty/malarnyje-raboty/?c=3097&lt=gallery&page=12',
    'https://natumbe.kz/almaty/malarnyje-raboty/?c=3097&lt=gallery&page=13',
    'https://natumbe.kz/almaty/malarnyje-raboty/?c=3097&lt=gallery&page=14',
    'https://natumbe.kz/almaty/malarnyje-raboty/?c=3097&lt=gallery&page=15',
    'https://natumbe.kz/almaty/santehnika-kommunikatsii/',
    'https://natumbe.kz/almaty/santehnika-kommunikatsii/?c=826&lt=gallery&page=2',
    'https://natumbe.kz/almaty/santehnika-kommunikatsii/?c=826&lt=gallery&page=3',
    'https://natumbe.kz/almaty/santehnika-kommunikatsii/?c=826&lt=gallery&page=4',
    'https://natumbe.kz/almaty/santehnika-kommunikatsii/?c=826&lt=gallery&page=5',
    'https://natumbe.kz/almaty/santehnika-kommunikatsii/?c=826&lt=gallery&page=6',
    'https://natumbe.kz/almaty/santehnika-kommunikatsii/?c=826&lt=gallery&page=7',
    'https://natumbe.kz/almaty/santehnika-kommunikatsii/?c=826&lt=gallery&page=8',
    'https://natumbe.kz/almaty/santehnika-kommunikatsii/?c=826&lt=gallery&page=9',
    'https://natumbe.kz/almaty/santehnika-kommunikatsii/?c=826&lt=gallery&page=10',
    'https://natumbe.kz/almaty/santehnika-kommunikatsii/?c=826&lt=gallery&page=11',
    'https://natumbe.kz/almaty/okna-dveri-balkony/',
    'https://natumbe.kz/almaty/okna-dveri-balkony/?c=825&lt=gallery&page=2',
    'https://natumbe.kz/almaty/okna-dveri-balkony/?c=825&lt=gallery&page=3',
    'https://natumbe.kz/almaty/krovelnyje-raboty/',
    'https://natumbe.kz/almaty/krovelnyje-raboty/?c=3093&lt=gallery&page=2',
    'https://natumbe.kz/almaty/krovelnyje-raboty/?c=3093&lt=gallery&page=3',
    'https://natumbe.kz/almaty/krovelnyje-raboty/?c=3093&lt=gallery&page=4',
    'https://natumbe.kz/almaty/krovelnyje-raboty/?c=3093&lt=gallery&page=5',
]


def get_html():
    links_db = []
    unique_links = []
    for url in URL:
        r = requests.get(url)
        print(r.status_code)
        soup = bs(r.text, 'lxml')
        card_links = soup.find_all('div', class_='it-grid-info')
        for toy in card_links:
            card_link = toy.find('div', class_='it-grid-mainfo').find('a').get('href')
            links_db.append(card_link)
        for item in links_db:
            if item not in unique_links:
                unique_links.append(item)
        with open('data_natumbe.txt', 'a') as file:
            for item in unique_links:
                file.write(item + '\n')
        print('done')


def main():
    chrome_options = webdriver.ChromeOptions()
    service = Service(executable_path=ChromeDriverManager().install())
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1200,900")
    chrome_options.add_argument("--disable-blink-features=AutomationConrtolled")
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                                " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.3")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    natumbe_db = []
    # with open('data_natumbe_unique.txt', 'r') as file:
    #     datas = file.read()
    #     for data in datas.split('\n'):
    #         try:
    #             driver.get(url)
    #             soup = bs(driver.page_source, 'lxml')
    #             sleep(50)
    data = 'https://natumbe.kz/almaty/uslugi-svarshhika-234099.html'
    driver.get(data)
    sleep(50)

def del_duplicate():
    with open('data_natumbe.txt', 'r') as file:
        lines = file.readlines()

    unique_lines = list(set(lines))

    with open('data_natumbe.txt', 'w') as file:
        file.writelines(unique_lines)


def get_unique():
    links_db = []
    with open('data_natumbe.txt', 'r') as file:
        lines = file.read()
        for line in lines.split('\n'):
            r = requests.get(line)
            print(r.status_code)
            soup = bs(r.text, 'lxml')
            name = soup.find('a', class_='vw-vendor-name').text
            if name == 'noname':
                pass
            else:
                links_db.append(line)
    with open('data_natumbe_unique.txt', 'a') as file:
        for line in links_db:
            file.write(line + '\n')
    print('done')

if __name__ == '__main__':
    # get_html()
    # main()
    # del_duplicate()
    get_unique()
