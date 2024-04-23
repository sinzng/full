#!/usr/bin/env python

salary = int(input("월급 입력: "))
income = 0
tax =0

#연봉 구하기
if salary >= 500:
    income = 12* salary
else :
    income = 13*salary
# 세금 구하기
if income >= 10000:
    tax = 0.2 * income
elif income >= 7000:
    tax = 0.15 * income
elif income >= 5000:
    tax = 0.12 * income
elif income >= 1000:
    tax = 0.1 * income
else :
    tax =0
print( f'월급 : {salary} ')
print( f'연봉 : {income} ')
print( f'세금 : {tax} ')

