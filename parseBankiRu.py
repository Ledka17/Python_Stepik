# pip install requests
# pip install pandas
# pip install time
# pip install ssl
# pip install bs4
# pip install lxml
# pip install openpyxl

import requests
from bs4 import BeautifulSoup
import pandas as pd
import ssl
import time as t

ssl._create_default_https_context = ssl._create_unverified_context

base_url = 'https://banki.ru'

company_urls = {
    '/insurance/responses/company/sberbankstrahovaniezhizni': 48,  # СБСЖ
    '/insurance/responses/company/sberbankstrahovanie': 16,  # СБС
    '/services/responses/bank/sberbank': 3394,  # СБ
}

page_url = '/?page='

df = pd.DataFrame(columns=['компания', 'url жалобы', 'Заголовок', 'Статус', 'Текст', 'Время', 'Оценка', 'Оценка выплат', 'Ответ', 'Время ответа'])

for company_url in company_urls.keys():
    print(company_url)

    company = company_url[company_url.rfind('/') + 1:]
    r = requests.get(base_url + company_url)
    soup = BeautifulSoup(r.text, features='lxml')

    pages = company_urls[company_url]

    for page in range(2, pages + 2):
        t.sleep(2)

        for article in soup.findAll('article'):
            try:
                rating_payouts = None
                rating_status = None
                answer = None
                answer_time = None

                href = article.find('a', {'data-test': 'responses-header'}).get('href')
                header = article.find('a', {'data-test': 'responses-header'}).text
                text = article.find('div', {'itemprop': 'description'}).text.strip()
                time = article.find('time', {'data-test': 'responses-datetime', 'itemprop': 'dtreviewed'}).get('datetime')
                rating = article.find('span', {'data-test': 'responses-rating-grade'}).text.strip()

                # optional

                try:
                    rating_payouts = article.find('strong', {'class': 'font-size-medium'}).text.strip()
                except:
                    pass
                try:
                    rating_status = article.find('span', {'data-test': 'responses-status'}).text.strip()
                except:
                    pass
                try:
                    answer = article.findAll('div', {'class': 'thread-item__text'})[-1].text
                    answer_time = article.findAll('time', {'class': 'thread-item__time'})[-1].get('datetime')
                except:
                    pass

                row = [company, base_url+href, header, rating_status, text, time, rating, rating_payouts, answer, answer_time]

                df.loc[len(df)] = row
            except:
                pass

        # Взятие следующей страницы
        try:
            if page <= pages:
                r = requests.get(base_url + company_url + page_url + str(page))
                soup = BeautifulSoup(r.text, features='lxml')
        except:
            pass

print(len(df))
df.to_excel('Жалобы_СБ.xlsx')
