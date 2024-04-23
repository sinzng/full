#!/usr/bin/env python

import pickle


class SmartPhone(object):
    def __init__(self, brand, maker, price): # __어쩌구__ : 기본 메서드
        self.brand = brand
        self.maker = maker
        self.price = price
    def __str__(self):
        return f'str: {self.brand} - {self.maker} - {self.price}'

object = SmartPhone("IPhone", "Apple", 10000)
f = open("test.pickle", "wb")
pickle.dump(object, f) # dump파일..백업파일..
f.close()

f = open("test.pickle", "rb")
object2 = pickle.load(f)
print(object2)
f.close()