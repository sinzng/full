#!/usr/bin/env python

import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc
from math import sqrt

# print([f.fname for f in matplotlib.font_manager.fontManager.ttflist])

# font_location = "C:\Windows\Fonts"
# font_name = font_manager.FontProperties(fname=font_location).get_name()
# matplotlib.rc('font.family'] = 'NanumBarunGothic'

plt.rcParams['font.family'] = 'NanumBarunGothic'

theaterfile = 'theater.csv'
colname = [ 'id', 'theater', 'region', 'bindo']
dftheater = pd.read_csv(theaterfile, names=colname, header=None)
dftheater = dftheater.rename(index= dftheater.id)
dftheater = dftheater.reindex(columns=['theater', 'region', 'bindo'])
dftheater.index.name = '영화제목' #설정 가능
print('전체 조회')
print(dftheater)
print('-'*50)

print('극장별 상영 횟수 집계')
mygrouping = dftheater.groupby('theater')['bindo']
sumSeries = mygrouping.sum()
meanSeries = mygrouping.mean()
sizeSeries = mygrouping.size()

print('시리즈 3개를 이용하여 데이터 프레임 생성')
df = pd.concat([sumSeries, meanSeries, sizeSeries], axis=1)
df.columns =['합계', '평균', '개수']
print(df)
print('-'*50)

mysize = len(mygrouping.groups)

df.plot(kind='barh', rot =0)
plt.title(str(mysize) + '개 매장 집계 데이터')
filename = 'p280_visualizationExam.png'
plt.savefig(filename)
# plt.show()


print('집계 함수를 dict에 담아 전달')
print('지역의 개수와 상영 횟수의 총합')
mydict = {'bindo': 'sum', 'region':'size' }
result = dftheater.groupby('theater').agg(mydict) # 집계 연산
print(result)
print('-'*50)

print('print using numpy')
result = mygrouping.agg([np.count_nonzero, np.mean, np.std])
print(result)
print('-'*50)

def myroot(values):
    mysum = sum(values)
    return sqrt(mysum)
def plus_add(values, somevalue):
    result =myroot(values)
    return result + somevalue

mygrouping = dftheater.groupby('theater')['bindo']
print('groupby와 사용자 정의 함수 사용')
result= mygrouping.agg(myroot)
print(result)
print('-'*50)

print('groupby와 사용자 정의 함수 사용(매개변수 2개 사용)')
result = mygrouping.agg(plus_add, somevalue=3)
print(result)
print('-'*50)

print('columns 2개 이상을 그룹핑하기')
newgrouping = dftheater.groupby(['theater', 'region'])['bindo']
result = newgrouping.count()
print(result)
print('-'*50)

newDF = df.loc[:, ['평균', '개수']]
newDF.plot(kind='bar', rot=0)
plt.title('3개 극장과 평균 상영관 수')
filename = 'p280_visualizationExam_02.png'
plt.savefig(filename)
print(filename + 'Saved...')
plt.show()

labels =[]
explode = (0,0.03, 0.06)

for key in sumSeries.index:
    mydata = key + '(' + str(sumSeries[key]) + ')'
    labels.append(mydata)

fig, ax1 = plt.subplots()
mytuple = tuple(labels)
ax1.pie(sumSeries, explode = explode, labels=mytuple,
        autopct='%1.1f%%', shadow =True, startangle=90)

ax1.axis('equal')
plt.show()
filename ='p280_visualizationExam_03.png'
plt.savefig(filename)
print(filename + 'Saved...')
print('finished')