#!/usr/bin/env python
while True:
    a = input("Input the number(q->quit):")

    if a == 'q':
        print("bye~~~~")
        break
    elif a.isalpha():
        print("다시 입력해주세요")
        continue
    else:
        if int(a) > 0 :
            print("This is positive")
        elif int(a) < 0 :
            print("This is negative")
        else  :
            print("This is zero")
