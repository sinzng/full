#!/usr/bin/env python

import random

def binary_digits(num, lists):
    q = num // 2
    r = num % 2
    lists.append(r)
    if q == 0 :
        lists.reverse()
        return lists
    else :
        return binary_digits(q, lists)

class BinaryDigits(object):
    def __init__(self, num, lists):
        self.num = num
        self.lists = lists

    # def bin(self):
    #     if self.num == 0:
    #         self.lists.reverse()
    #         return self.lists
    #     else :
    #         return bin(self.num)
    def convert(self):
        q = self.num
        lists = self.lists
        while True:
            r = q % 2
            q = q//2
            lists.append(r)
            if q == 0 :
                break
        lists.reverse()
        return lists

lists = []
num = random.randint(4,16)
bin = BinaryDigits(num, lists)
print(f'{num} binary number is : {bin.convert()}')
