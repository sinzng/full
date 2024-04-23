#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'NanumBarunGothic'

filename = 'mygraph.csv'

myframe = pd.read_csv(filename,index_col='이름', encoding='utf-8')
myframe.index.name = '학생이름'
myframe.columns.name= '시험과목'

myframe.plot(kind = 'bar', rot =0, stacked=True, title='학생별 시험 점수', legend = True)

print(myframe)
print('-'*50)

filename = 'Ex_p239_Graph02_04.png'
plt.savefig(filename, dpi=400, bbox_inches = 'tight')
print(filename + 'Saved....')
print('-'*50)

plt.show()
