#!/usr/bin/env python

somelist = ['김의찬', '유만식','이영철','심수련', '윤기석', '노윤희', '황우철']

print(somelist)
print(somelist[4])
print(somelist[-2])
print(somelist[1:4])
print(somelist[4:])
length = len(somelist)
print(length)
print(somelist[:length:2]) # 김의찬 이영철 윤기석 황우철 (length가 7이니까 인덱스6까지 출력)
print(somelist[1:length:2]) # 유만식 심수련 노윤희