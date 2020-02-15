import requests
from bs4 import BeautifulSoup
#  from lxml import html
import pandas as pd
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

base_url = 'https://nsddata.ru'
url_next_page = '/ru/refbooks/securities?SecuritySearch%5Bissuer%5D=&SecuritySearch%5BfinInstrumentTypeId%5D=&SecuritySearch%5BcdListTypes%5D=&SecuritySearch%5BforQIOnly%5D=Y&SecuritySearch%5BsecCode%5D=&SecuritySearch%5BcodeFields%5D=&SecuritySearch%5BcodeFields%5D%5B%5D=state_reg_number&SecuritySearch%5BcodeFields%5D%5B%5D=identific_number&SecuritySearch%5BcodeFields%5D%5B%5D=state_reg_number_rule&SecuritySearch%5BcodeFields%5D%5B%5D=state_reg_number_isu&SecuritySearch%5BcodeFields%5D%5B%5D=isin&SecuritySearch%5BcodeFields%5D%5B%5D=code_ndc&SecuritySearch%5BcodeFields%5D%5B%5D=4%2C19%2C21%2C37&SecuritySearch%5BcodeFields%5D%5B%5D=3&SecuritySearch%5BcodeFields%5D%5B%5D=8&SecuritySearch%5BcodeFields%5D%5B%5D=7' # url для второй страницы
df = pd.DataFrame()

for i in range(1158):
  print(i)
  r = requests.get(base_url + url_next_page)
  #  with open('test.html', 'w') as output_file:
  #  output_file.write(str(r.text.encode('utf-8'), encoding="utf-8"))

  soup = BeautifulSoup(r.text, features="lxml")
  #  cb_list = soup.find('div', {'class': 'container_content'})

  #  tree = html.fromstring(r.text)  # весь код html страницы

  url_next_page = soup.find('li', {'class': 'next'}).find('a').get('href')

  #  print(r.text)

  pull_df, = pd.read_html(base_url + url_next_page)
  df = pd.concat([df, pull_df])
  url_next_page = soup.find('li', {'class': 'next'}).find('a').get('href')

df.to_excel('nsdata_full.xlsx')
#  print(url_next_page)
