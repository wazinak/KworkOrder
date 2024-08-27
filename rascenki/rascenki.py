from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

URL = [
    'https://rascenki.kz/ads/cat/stroitelnye_raboty/city/almaty/',
    'https://rascenki.kz/ads/cat/stroitelnye_raboty/city/almaty/page/2/',
    'https://rascenki.kz/ads/cat/krovelnye_raboty/region/almatinskaya_oblast/',
    'https://rascenki.kz/ads/cat/krovelnye_raboty/region/almatinskaya_oblast/page/2/',
    'https://rascenki.kz/ads/cat/elektromontazhnye_raboty/region/almatinskaya_oblast/',
    'https://rascenki.kz/ads/cat/elektromontazhnye_raboty/region/almatinskaya_oblast/page/2/',
    'https://rascenki.kz/ads/cat/stroitelstvo_derevyannyx_domov/region/almatinskaya_oblast/',
    'https://rascenki.kz/ads/cat/stroitelnye_raboty/region/almatinskaya_oblast/',
    'https://rascenki.kz/ads/cat/stroitelnye_raboty/region/almatinskaya_oblast/page/2/',
    'https://rascenki.kz/ads/cat/stroitelnye_raboty/region/almatinskaya_oblast/page/3/',
    'https://rascenki.kz/ads/cat/santexnicheskie_raboty/region/almatinskaya_oblast/',
    'https://rascenki.kz/ads/cat/santexnicheskie_raboty/region/almatinskaya_oblast/page/2/',
    'https://rascenki.kz/ads/cat/santexnicheskie_raboty/region/almatinskaya_oblast/page/3/',
    'https://rascenki.kz/ads/cat/santexnicheskie_raboty/region/almatinskaya_oblast/page/4/',
    'https://rascenki.kz/ads/cat/remontno-stroitelnye_raboty/region/almatinskaya_oblast/',
    'https://rascenki.kz/ads/cat/remontno-stroitelnye_raboty/region/almatinskaya_oblast/page/2/',
    'https://rascenki.kz/ads/cat/remontno-stroitelnye_raboty/region/almatinskaya_oblast/page/3/',
    'https://rascenki.kz/ads/cat/remontno-stroitelnye_raboty/region/almatinskaya_oblast/page/4/',
    'https://rascenki.kz/ads/cat/remontno-stroitelnye_raboty/region/almatinskaya_oblast/page/5/',
    'https://rascenki.kz/ads/cat/remont_kvartir/region/almatinskaya_oblast/',
    'https://rascenki.kz/ads/cat/remont_kvartir/region/almatinskaya_oblast/page/2/',
    'https://rascenki.kz/ads/cat/remont_kvartir/region/almatinskaya_oblast/page/3/',
    'https://rascenki.kz/ads/cat/remont_kvartir/region/almatinskaya_oblast/page/4/',
    'https://rascenki.kz/ads/cat/remont_kvartir/region/almatinskaya_oblast/page/5/',
    'https://rascenki.kz/ads/cat/remont_kvartir/region/almatinskaya_oblast/page/6/',
    'https://rascenki.kz/ads/cat/remont_kvartir/region/almatinskaya_oblast/page/7/',
    'https://rascenki.kz/ads/cat/remont_kvartir/region/almatinskaya_oblast/page/8/',
    'https://rascenki.kz/ads/cat/remont_kvartir/region/almatinskaya_oblast/page/9/',
    'https://rascenki.kz/ads/cat/remont_kvartir/region/almatinskaya_oblast/page/10/',
    'https://rascenki.kz/ads/cat/remont_kvartir/region/almatinskaya_oblast/page/11/',
    'https://rascenki.kz/ads/cat/remont_kvartir/region/almatinskaya_oblast/page/12/',
    'https://rascenki.kz/ads/cat/remont_kvartir/region/almatinskaya_oblast/page/13/',
    'https://rascenki.kz/ads/cat/pokrasochnye_raboty/region/almatinskaya_oblast/',
    'https://rascenki.kz/ads/cat/plotnickie_raboty/region/almatinskaya_oblast/',
    'https://rascenki.kz/ads/cat/plitochnye_raboty/region/almatinskaya_oblast/',
    'https://rascenki.kz/ads/cat/otdelochnye_raboty/region/almatinskaya_oblast/',
    'https://rascenki.kz/ads/cat/otdelochnye_raboty/region/almatinskaya_oblast/page/2/',
    'https://rascenki.kz/ads/cat/otdelochnye_raboty/region/almatinskaya_oblast/page/3/',
    'https://rascenki.kz/ads/cat/otdelochnye_raboty/region/almatinskaya_oblast/page/4/',
    'https://rascenki.kz/ads/cat/otdelochnye_raboty/region/almatinskaya_oblast/page/5/',
    'https://rascenki.kz/ads/cat/obtshestroitelnye_raboty/region/almatinskaya_oblast/',
    'https://rascenki.kz/ads/cat/obtshestroitelnye_raboty/region/almatinskaya_oblast/page/2/',
    'https://rascenki.kz/ads/cat/naruzhnye_raboty/region/almatinskaya_oblast/',
    'https://rascenki.kz/ads/cat/montazhnye_raboty/region/almatinskaya_oblast/',
    'https://rascenki.kz/ads/cat/montazhnye_raboty/region/almatinskaya_oblast/page/2/',
    'https://rascenki.kz/ads/cat/montazhnye_raboty/region/almatinskaya_oblast/page/3/',
    'https://rascenki.kz/ads/cat/montazhnye_raboty/region/almatinskaya_oblast/page/4/',
    'https://rascenki.kz/ads/cat/montazhnye_raboty/region/almatinskaya_oblast/page/5/',
    'https://rascenki.kz/ads/cat/malyarnye_rabty/region/almatinskaya_oblast/',
    'https://rascenki.kz/ads/cat/malyarnye_rabty/region/almatinskaya_oblast/page/2/',
]


def getting_link_from_pages():
    """ Функция получает ссылки из страниц"""
    links_db = []
    unique_links = []
    for link in URL:
        r = requests.get(link)
        print(r.status_code)
        soup = bs(r.text, 'lxml')
        card_links = soup.find_all('div', class_='all_ads')
        for card_link in card_links:
            urls = card_link.find('a').get('href')
            links_db.append(urls)
        for item in links_db:
            if item not in unique_links:
                unique_links.append(item)
        with open('data_rascenki.txt', 'a') as file:
            for item in unique_links:
                file.write(item + '\n')
        print('done')


def main():
    rascenki = []
    with open('data_rascenki.txt', 'r') as file:
        datas = file.read()
    try:
        for url in datas.split('\n'):
            r = requests.get(url)
            print(r.status_code)
            soup = bs(r.text, 'lxml')
            phone = soup.find_all('p')[2].text.replace('Телефон: ', '')
            name = soup.find_all('p')[1].text.replace('Автор: ', '')
            print(name)
            description = soup.find_all('p')[5].text.replace('Текстобъявления: ', '')
            rascenki.append(
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
    df_admir = pd.DataFrame(rascenki)
    csv_name = 'data_rascenki.csv'
    df_admir.to_csv(csv_name, index=False)


if __name__ == '__main__':
    # getting_link_from_pages()
    main()
