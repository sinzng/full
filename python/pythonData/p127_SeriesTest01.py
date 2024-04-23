#!/usr/bin/env python
from pandas import Series

mylist = [10,20,30,40]
myseries = Series(data= mylist, index=['김유신','이순신','강감찬','광해군'])

print('\n Data Type')
print(type(myseries))

myseries.index.name = '점수' # 인덱스의 이름
print('\n Index name of Seres')
print(myseries.index.name)

print('\n name of Seres')
print(myseries.index)

print('\n value of Seres')
print(myseries.values)

print('\n print informational of Seres')
print(myseries)

print('\n repeat print')
for idx in myseries.index:
    print('index : ' + idx + ', Values : ' + str(myseries[idx]))


