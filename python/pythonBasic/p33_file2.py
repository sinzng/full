#!/usr/bin/env python

f = open('test.txt', 'w')
f.write("This file is %s \n" % ("test.txt"))
f.write("end of file")
f.close()
f = open('test.txt', 'r')
line = 1
while line:
    line = f.readline()
    print(line)
f.close()