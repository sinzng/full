#!/usr/bin/env python

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

print('\n # series의 누락 데이터 처리')
print('\n # 원본 seires')
myseries = Series(['강감찬','이순신',np.nan, '광해군'])
print(myseries)

print('\n # isnull() 함수 : NaN 이면 True')
print(myseries.isnull())
print('-'*50)

print('\n # notnull() 함수 : NaN이 아니면 True')
print(myseries.notnull())
print('-'*50)

print('\n # notnull() 이용해서 참인 항목만 출력')
print(myseries[myseries.notnull()])
print('-'*50)

print('\n # dropna() 이용 누락 데이터')
print(myseries.dropna())
print('-'*50)

filename = 'excel02.csv'
myframe = pd.read_csv(filename, index_col='이름', encoding='utf-8')
print('\n', myframe)

print('\n # dropna() 이용 누락 데이터 처리')
cleaned = myframe.dropna(axis=0)
print('\n', cleaned)
print('-'*50)

print('\n # how="all" 이용 누락 데이터 처리')
cleaned = myframe.dropna(axis=0, how='all')
print('\n', cleaned)
print('-'*50)

print('\n # how="any" 이용 누락 데이터 처리')
cleaned = myframe.dropna(axis=0, how='any') # axis=0 은 row 기준
print('\n', cleaned)
print('-'*50)

print('\n # [영어] columns 누락 데이터 처리 ')
print(myframe.dropna(subset=['영어']))
print('-'*50)

print('\n # how="all" 이용 누락 데이터 처리')
cleaned = myframe.dropna(axis=1, how='all') # axis=1 은 column 기준
print('\n', cleaned)
print('-'*50)

print('\n # how="any" 이용 누락 데이터 처리')
cleaned = myframe.dropna(axis=1, how='any') # axis=1 은 column 기준
print('\n', cleaned)
print('-'*50)

print(myframe)
myframe.loc[['강감찬','홍길동'], ['국어']] = np.nan
print(' ## after ## ')
print(myframe)

print(myframe.dropna(axis=1, how='all'))

print(' ## thresh option')
print(myframe.dropna(axis=1, thresh=2)) # NaN이 두개인 컬럼 출력
print('-'*50)

print(myframe.dropna(axis=1, how='any'))
print('-'*50)

