#!/usr/bin/env python

class Factorial(object):
    def __init__(self, x):
        self.x = x
    def f(self):
        n = 1
        for i in range(1, self.x + 1):
            n *= i
        return n #재귀호출 안하는 팩토리얼 코드
a = int(input("Enter a number: "))
fact = Factorial(a)
print(f'{input} factorial ={fact.f()}')