#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'NanumBarunGothic'

filename = '점수데이터.csv'
myframe = pd.read_csv(filename, encoding='utf-8', index_col=0)
# index_col은 데이터프레임을 생성할 때 어떤 열을 인덱스로 지정할 것인지를 결정하는 매개변수

print(myframe['jumsu'].unique())

frame01 = myframe.loc[myframe['jumsu'] == 'lower', 'length']
frame01.index.name = 'lower'
print(frame01.head())
print('-'*50)

frame02 = myframe.loc[myframe['jumsu'] == 'upper', 'length']
frame02.index.name = 'upper'
print(frame02.head())
print('-'*50)

totalframe = pd.concat([frame01, frame02], axis=1, ignore_index=True)
totalframe.columns = ['lower', 'upper']
print(totalframe.head())
print('-'*50)

totalframe.plot(kind='box')

plt.xlabel('점수구분')
plt.ylabel('길이')
plt.grid(False)
plt.title("점수에 따른 길이의 상자 수염 그래프")

filename = 'boxPlot01.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + 'Saved...')
plt.show()