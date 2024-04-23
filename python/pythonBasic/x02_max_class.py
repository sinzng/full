#!/usr/bin/env python

import random
data = random.sample(range(1,101), 10)
print(data)
class findMax(object):
    def __init__(self, data):
        self.data = data
    def max(self):
        return max(self.data)
a = findMax(data)
print("Max value is : ", a.max())