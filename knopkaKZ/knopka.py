from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pandas as pd
from time import sleep


chrome_options = webdriver.ChromeOptions()
service = Service(executable_path=ChromeDriverManager().install())
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1200,900")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument("--disable-blink-features=AutomationConrtolled")
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                            " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.3")
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    'source': '''
            delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
            delete window.cdc_adoQpoasnfa76pfcZLmcfl_JSON;
            delete window.cdc_adoQpoasnfa76pfcZLmcfl_Object;
            delete window.cdc_adoQpoasnfa76pfcZLmcfl_JSON;
            delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
            delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;

            '''
})


URL = [
    'https://knopka.kz/almaty/rabota/ishhu-rabotu-rezume/?lt=gallery&cur=5',
    'https://knopka.kz/almaty/uslugi-soobshhenija/stroitelnyje-i-otdelochnyje-raboty/',
]

link = 'https://knopka.kz/almaty/uslugi-soobshhenija/stroitelnyje-i-otdelochnyje-raboty/'


def getting_links():

    driver.get(link)

    sleep(30)



if __name__ == '__main__':
    getting_links()
