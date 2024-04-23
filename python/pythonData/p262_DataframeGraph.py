#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'NanumBarunGothic'

filename = 'ex802.csv'

myframe = pd.read_csv(filename, index_col ='type', encoding='utf-8')
myframe.index.name = '자동차 유형'
myframe.columns.name= '도시(city)'

myframe.plot(kind = 'bar', rot =0, title='지역별 차량 등록 대수', legend = True)

print(myframe)
print('-'*50)

filename = 'dataFrameGraph02_01.png'
plt.savefig(filename, dpi=400, bbox_inches = 'tight')
print(filename + 'Saved....')

myframeT =myframe.T # .T는 데이터프레임의 전치(transpose)를 수행
print(myframeT)
print('-'*50)

ymax = myframeT.sum(axis=1)
ymaxlimit = ymax.max() +10

myframeT.plot(kind='bar',ylim=[0, ymaxlimit], rot=0, stacked=True, title='지역별 차 ', legend=True)
filename = 'dataFrameGraph02_02.png'
plt.savefig(filename, dpi=400, bbox_inches = 'tight')
print(filename + 'Saved....')
print('-'*50)

plt.show()
