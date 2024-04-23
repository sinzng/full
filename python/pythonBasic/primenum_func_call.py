#!/usr/bin/env python

import prime_func

while True:
    num = int(input("Enter a number: "))
    if num == 0 :
        break
    if (num <2) :
        print(num, "re enter number")
        continue
    print(f"{num}is prime number")if prime_func.prime(num) == 1 else print(f"{num} is not prime number")