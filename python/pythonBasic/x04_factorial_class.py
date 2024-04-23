#!/usr/bin/env python

class Factorial(object):
    def __init__(self, x):
        self.x = x
    def f(self):
        if self.x == 0 :
            return 1
        else:
            n = self.x
            self.x -= 1
            return n * self.f()

a = int(input("Enter a number: "))
fact = Factorial(a)
print(f'{input} factorial ={fact.f()}')