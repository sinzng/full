#!/usr/bin/env python

import numpy as np
import pandas as pd
from pandas import Series

flilname = '과일매출현황.csv'
df = pd.read_csv(flilname, index_col='과일명')
print('\n 원본 데이터프레임')
print(df)

df.loc[df['구입액'].isnull(),['구입액']] =50.00
df.loc[df['수입량'].isnull(),['수입량']] =20.00
print(df)
print('-'*50)
print('\n # 구입액과 수입량의 소계')
print(df.sum(axis=0))
print('-'*50)

print('\n # 과일별 소계')
print(df.sum(axis=1))
print('-'*50)

print('\n # 구입액과 수입량의 평균')
print(df.mean(axis=0))
print('-'*50)

print('\n # 과일별 평균')
print(df.mean(axis=1))
print('-'*50)


