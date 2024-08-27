from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pandas as pd
from time import sleep
import easyocr


chrome_options = webdriver.ChromeOptions()
service = Service(executable_path=ChromeDriverManager().install())
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1200,900")
chrome_options.add_argument("--disable-blink-features=AutomationConrtolled")
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                            " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.3")
driver = webdriver.Chrome(service=service, options=chrome_options)

reader = easyocr.Reader(['en'])



URL = [
    'https://avi.kz/almaty/uslugi/stroitelstvo-otdelka-remont/stroitelnye-uslugi/',
    'https://avi.kz/almaty/uslugi/stroitelstvo-otdelka-remont/stroitelnye-uslugi/?lt=1&page=2',
    'https://avi.kz/almaty/uslugi/stroitelstvo-otdelka-remont/stroitelnye-uslugi/?lt=1&page=3',
    'https://avi.kz/almaty/uslugi/stroitelstvo-otdelka-remont/stroitelnye-uslugi/?lt=1&page=4',
]


def getting_links():
    links_db = []
    unique_links = []
    for url in URL:
        print(url)
        sleep(1)
        r = requests.get(url)
        print(r.status_code)
        soup = bs(r.text, 'lxml')
        card_links = soup.find_all('div', class_='sr-2-list-item-n')
        for link in card_links:
            href = link.find('a').get('href')
            links_db.append(href)
        for item in links_db:
            if item not in unique_links:
                unique_links.append(item)
        with open('data_avi.txt', 'a') as file:
            for item in unique_links:
                file.write(item + '\n')
        print('done')


def main():
    avi_db = []
    with open('data_avi.txt', 'r') as file:
        datas = file.read()
        for data in datas.split('\n'):
            try:
                driver.get(data)
                sleep(1)
                btn = driver.find_element('xpath', '/html/body/div[2]/div[5]/div/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/a')
                driver.execute_script("arguments[0].scrollIntoView();", btn)
                btn.click()
                sleep(2)
                soup = bs(driver.page_source, 'lxml')
                try:
                    name = soup.find('div', class_='v-author__info').find('span').text.strip()
                    description = soup.find('div', class_='v-descr_text').text.strip()
                    phone_url = driver.find_element('xpath', '//*[@id="j-view-container"]/div[1]/div/div[3]/div/div[1]/div[4]/div[2]/div[2]/div/div/span/img').get_attribute('src')
                    driver.get(phone_url)
                    screenshot = driver.get_screenshot_as_png()
                    screenshot_name = data.split('/')[-1].split('.')[0].split('-')[-1]
                    with open(f'screenshots/screenshot_{screenshot_name}.png', 'wb') as file:
                        file.write(screenshot)
                    phone = reader.readtext(f'screenshots/screenshot_{screenshot_name}.png', detail=0)[0]
                    avi_db.append({
                        'phone': phone,
                        'name': name,
                        'description': description,
                    })
                except Exception as e:
                    pass
            except Exception as e:
                continue
    df_avi = pd.DataFrame(avi_db)
    df_avi.to_csv('data_avi.csv')
    print('done')


# TODO запустить скрипт


if __name__ == '__main__':
    # getting_links()
    main()