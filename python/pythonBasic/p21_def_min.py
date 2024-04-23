#!/usr/bin/env python

def min(a, b):
    if a>b:
        return b
    else:
        return a

a = input("input the number: ")
b = input("input the number: ")

print("{} vs {} : Min number = {}".format(a,b,min(a,b)))