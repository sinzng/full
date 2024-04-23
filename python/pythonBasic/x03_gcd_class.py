#!/usr/bin/env python

import random

class gcdClass(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def gcd(self):
        while self.b != 0:
            r = self.a % self.b
            self.a = self.b
            self.b = r
        return self.a

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

gcd1 = gcdClass(a, b)
print(f'gcd({a}, {b} of {a}, {b}) = {gcd1.gcd()}')