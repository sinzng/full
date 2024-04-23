#!/usr/bin/env python

import re

mylist = [ 'ab123', 'cd345', 'ef789', 'abc12']

regex = ('[a-z]{2}\d{3}') #알바펫이 두개 숫자가 세개
pattern = re.compile(regex)

print('#문자열 2개, 숫자 3개 패턴 찾기')
totallist = []
for item in mylist:
    if pattern.match(item):
        print(item, '은(는) 조건에 적합')
        totallist.append(item)
    else :
        print(item, '은(는) 조건에 부적합')
print('\n조건에 적합한 항목들')
print(totallist)