#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'NanumBarunGothic'

filename = 'mpg.csv'
myframe = pd.read_csv(filename, encoding='utf-8')
# index_col은 데이터프레임을 생성할 때 어떤 열을 인덱스로 지정할 것인지를 결정하는 매개변수

print(myframe['drv'].unique())

frame01 = myframe.loc[myframe['drv'] == 'f', 'hwy']
frame01.index.name = '전륜'
print(frame01.head())
print('-'*50)

frame02 = myframe.loc[myframe['drv'] == '4', 'hwy']
frame02.index.name = '사륜'
print(frame02.head())
print('-'*50)

frame03 = myframe.loc[myframe['drv'] == 'r', 'hwy']
frame03.index.name = '후륜'
print(frame03.head())
print('-'*50)

totalframe = pd.concat([frame01, frame02, frame03], axis=1, ignore_index=True)
totalframe.columns = ['f', '4', 'r']
print(totalframe.head())
print('-'*50)

totalframe.plot(kind='box')

plt.xlabel('구동방식')
plt.ylabel('주행마일수')
plt.grid(False)
plt.title("고속도로 주행 마일수의 상자 수염")

filename = 'boxPlot03.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + 'Saved...')
plt.show()