#!/usr/bin/env python

import pandas as pd
from pandas import Series
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'NanumBarunGothic'
#print([f.fname for f in matplotlib.font_manager.fontManager.ttflist])

filenname = 'ex802.csv'
df = pd.read_csv(filenname, index_col='type',encoding='utf-8')
df.plot(title='지역별 차종 교통량', kind='line', rot=0, legend=True)
print(df)

file = 'Ex_p289_04.png'
plt.savefig(file, dpi=400, bbox_inches='tight')
print(file + 'Saved...')
plt.show()