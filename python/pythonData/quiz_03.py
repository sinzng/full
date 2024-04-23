#!/usr/bin/env python

import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'NanumBarunGothic'

url = 'https://www.moviechart.co.kr/rank/boxoffice'
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

infos = soup.findAll('div', attrs={'class': 'wArea space title'})
# print(infos)

mydata0 = [i for i in range(1, 20)]

# print(mydata0)

result = []
title = soup.select("td.title > a")
for i in title:
    result.append(i.text.replace(' ',''))
mydata1 = result
print(mydata1)

result = []
aud = soup.select("td.audience")
for i in aud:
    result.append(i.text.replace(' ','').replace(',','').strip('명\r\n'))
mydata2 = result
print(mydata2)

result = []
cum = soup.select("td.cumulative")
for i in cum:
    result.append(i.text.replace(' ','').replace(',','').strip('명\r\n'))
mydata3 = result
print(mydata3)

mycolumn = ['순위','제목', '관객수', '누적관객수']

myframe = pd.DataFrame(data = list(zip(mydata0, mydata1, mydata2, mydata3)), columns = mycolumn)
df = myframe.set_index(keys=['순위'])
print(df)
print('-' * 40)

filename = 'Movie.csv'
myframe.to_csv(filename, encoding='utf8', index=False)
print(filename, ' saved...', sep='')
print('finished')

dfmovie = myframe.reindex(columns=['관객수', '누적관객수'])
print(dfmovie)

dfmovie.astype(float).plot(kind='barh', title='영화별 평점과 예매율', rot=0)
filename = 'MovieGraph.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
plt.show()
