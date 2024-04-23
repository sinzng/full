#!/usr/bin/env python

class Person(object):
    total = 10
    def __init__(self, name, age): # init으로 초기화
        self.name = name
        self.age =  age
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
my = Person('Shin','20')
print(my.name)
print(my.age)
print(my.getName())
print(my.getAge())
print(f'total: {my.total}')

you = Person('Kim','30')
print(you.getName())
print(you.getAge())
print(f'total: {you.total}')