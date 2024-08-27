from bs4 import BeautifulSoup as bs
import requests
import pandas as pd


def getting_links():
    """функция получает все ссылки с двух страниц со сайта объявлений"""
    unique_links = []
    links_urls_1 = []
    for p in range(11):
        url_1 = f'https://almaty.admir.kz/ru-i-classifieds-i-page-i-{p}-1-i-category-i-stroitelinye-raboty-i-p.html'
        r = requests.get(url_1)
        print(r.status_code)
        soup = bs(r.text, 'lxml')
        links = soup.find_all('a', class_='text-dark mb-2')
        for link in links:
            link_card = link.get('href')
            links_urls_1.append(link_card)
    for i in range(11):
        url_2 = f'https://almaty.admir.kz/ru-i-classifieds-i-page-i-{i}-1-i-category-i-proektirovanie-dizajn-i-p.html'
        r = requests.get(url_2)
        print(r.status_code)
        soup = bs(r.text, 'lxml')
        links = soup.find_all('a', class_='text-dark mb-2')
        for link in links:
            link_card = link.get('href')
            links_urls_1.append(link_card)
    for item in links_urls_1:
        if item not in unique_links:
            unique_links.append(item)
    with open('data_admir.txt', 'a') as file:
        for item in unique_links:
            file.write(item + '\n')
    print('done')


def parsing_links_admir():
    """  функция парсит ссылки и сохраняет в файл"""
    admir_db = []
    unique_admir_db = []
    with open('data_admir.txt', 'r') as file:
        datas = file.read()
    try:
        for url in datas.split('\n'):
            r = requests.get(url)
            print(r.status_code)
            soup = bs(r.text, 'lxml')
            phone = soup.find('div', class_='card-body item-user').find_all('div')[2].text
            name = soup.find('div', class_='card-header').text.strip()
            description = soup.find_all('p')[0].text.strip()
            admir_db.append(
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
    for info in admir_db:
        if info not in unique_admir_db:
            unique_admir_db.append(info)
    df_admir = pd.DataFrame(unique_admir_db)
    csv_name = 'data_admir.csv'
    df_admir.to_csv(csv_name, index=False)


if __name__ == '__main__':
    # getting_links()
    parsing_links_admir()
