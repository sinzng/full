#!/usr/bin/env python

import pandas as pd
from pandas import Series
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'NanumBarunGothic'
#print([f.fname for f in matplotlib.font_manager.fontManager.ttflist])

filenname = 'dataframeGraph.csv'
df = pd.read_csv(filenname)
df = df.set_index(keys='name')
print(df)
print('-'*50)

df.plot(title='someTitle', kind='line',figsize=(10,6), legend=True)
file = 'p289_seriesGraph02.png'
plt.savefig(file, dpi=400, bbox_inches='tight')
print(file + 'Saved...')
plt.show()