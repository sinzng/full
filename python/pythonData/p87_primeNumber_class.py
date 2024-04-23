#!/usr/bin/env python

import random

class Prime(object):
    def __init__(self,num):
        self.num = num

    def isPrime(self):
        for k in range(2,self.num+1):
            if self.num % k == 0:
                break
        if k == self.num:
            return True
        else :
            return False

number = random.randint(2, 10)
prime = Prime(number)
print(f'{prime.num} is prime numbers') if prime.isPrime() else print(f'{prime.num} is not prime numbers')