from bs4 import BeautifulSoup as bs
import requests
import pandas as pd


URL = [
    'https://almaty.i-r.kz/ads-i-category-i-cantehnika-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-2-1-i-category-i-cantehnika-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-3-1-i-category-i-cantehnika-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-4-1-i-category-i-cantehnika-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-5-1-i-category-i-cantehnika-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-6-2-i-category-i-cantehnika-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-7-2-i-category-i-cantehnika-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-8-2-i-category-i-cantehnika-i-p.html',
    'https://almaty.i-r.kz/ads-i-category-i-ojtoplenie-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-2-1-i-category-i-ojtoplenie-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-3-1-i-category-i-ojtoplenie-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-4-1-i-category-i-ojtoplenie-i-p.html',
    'https://almaty.i-r.kz/ads-i-category-i-ventiljatsija--i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-2-1-i-category-i-ventiljatsija--i-p.html',
    'https://almaty.i-r.kz/ads-i-category-i-okna-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-2-1-i-category-i-okna-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-3-1-i-category-i-okna-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-4-1-i-category-i-okna-i-p.html',
    'https://almaty.i-r.kz/ads-i-category-i-parket-laminat-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-2-1-i-category-i-parket-laminat-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-3-1-i-category-i-parket-laminat-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-4-1-i-category-i-parket-laminat-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-5-1-i-category-i-parket-laminat-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-6-2-i-category-i-parket-laminat-i-p.html',
    'https://almaty.i-r.kz/ads-i-category-i-proektirovanie-dizajn-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-2-1-i-category-i-proektirovanie-dizajn-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-3-1-i-category-i-proektirovanie-dizajn-i-p.html',
    'https://almaty.i-r.kz/ads-i-category-i-elektrika-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-2-1-i-category-i-elektrika-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-3-1-i-category-i-elektrika-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-4-1-i-category-i-elektrika-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-5-1-i-category-i-elektrika-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-6-2-i-category-i-elektrika-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-7-2-i-category-i-elektrika-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-8-2-i-category-i-elektrika-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-9-2-i-category-i-elektrika-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-10-2-i-category-i-elektrika-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-11-3-i-category-i-elektrika-i-p.html',
    'https://almaty.i-r.kz/ads-i-category-i-otdelochnye-materialy-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-2-1-i-category-i-otdelochnye-materialy-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-3-1-i-category-i-otdelochnye-materialy-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-4-1-i-category-i-otdelochnye-materialy-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-5-1-i-category-i-otdelochnye-materialy-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-6-2-i-category-i-otdelochnye-materialy-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-7-2-i-category-i-otdelochnye-materialy-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-8-2-i-category-i-otdelochnye-materialy-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-9-2-i-category-i-otdelochnye-materialy-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-10-2-i-category-i-otdelochnye-materialy-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-11-3-i-category-i-otdelochnye-materialy-i-p.html',
    'https://almaty.i-r.kz/ads-i-category-i-stroitelinye-raboty-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-2-1-i-category-i-stroitelinye-raboty-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-3-1-i-category-i-stroitelinye-raboty-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-4-1-i-category-i-stroitelinye-raboty-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-5-1-i-category-i-stroitelinye-raboty-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-6-2-i-category-i-stroitelinye-raboty-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-7-2-i-category-i-stroitelinye-raboty-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-8-2-i-category-i-stroitelinye-raboty-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-9-2-i-category-i-stroitelinye-raboty-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-10-2-i-category-i-stroitelinye-raboty-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-11-3-i-category-i-stroitelinye-raboty-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-12-3-i-category-i-stroitelinye-raboty-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-13-3-i-category-i-stroitelinye-raboty-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-14-3-i-category-i-stroitelinye-raboty-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-15-3-i-category-i-stroitelinye-raboty-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-16-4-i-category-i-stroitelinye-raboty-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-17-4-i-category-i-stroitelinye-raboty-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-18-4-i-category-i-stroitelinye-raboty-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-19-4-i-category-i-stroitelinye-raboty-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-20-4-i-category-i-stroitelinye-raboty-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-21-5-i-category-i-stroitelinye-raboty-i-p.html',
    'https://almaty.i-r.kz/ads-i-page-i-22-5-i-category-i-stroitelinye-raboty-i-p.html',
    '',
    '',
    '',
    '',
    '',
]


def get_urls():
    """  собираем все ссылки на страницу"""
    links_db = []
    unique_links = []
    for url in URL:
        r = requests.get(url)
        print(r.status_code)
        soup = bs(r.text, 'lxml')
        card_links = soup.find('div', class_='item-card2-desc').find('a').get('href')
        links_db.append(card_links)
        for item in links_db:
            if item not in unique_links:
                unique_links.append(item)
        with open('data_ir.txt', 'a') as file:
            for item in unique_links:
                file.write(item + '\n')
        print('done')


def main():
    """  парсим страницу  """
    ir_db = []
    with open('data_ir.txt', 'r') as file:
        datas = file.read()
    try:
        for url in datas.split('\n'):
            r = requests.get(url)
            print(r.status_code)
            soup = bs(r.text, 'lxml')
            phone = soup.find('a', class_='text-primary').text
            name = soup.find('h3', class_='card-title').text.strip()
            description = soup.find('div', class_='card-body').find('div', class_='mb-4').text.strip()
            ir_db.append(
                {
                    'phone': phone,
                    'name': name,
                    'description': description,
                }
            )
            print('done')
    except Exception as e:
        print(e)
        pass
    df_ir = pd.DataFrame(ir_db)
    csv_name = 'data_ir.csv'
    df_ir.to_csv(csv_name, index=False)


if __name__ == '__main__':
    # get_urls()
    main()
