#!/usr/bin/env python

import random
data = random.sample(range(1,101), 10)
print(data)
def findMax(data):
    print("Max value is :", max(data))

findMax(data)