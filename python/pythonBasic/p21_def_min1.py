#!/usr/bin/env python

def min(a, b):
    return b if a < b else a

a = input("input the number: ")
b = input("input the number: ")

print("{} vs {} : Min number = {}".format(a,b,min(a,b)))