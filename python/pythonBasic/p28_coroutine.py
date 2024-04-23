#!/usr/bin/env python

def handler():
    print('Initialize Handler')
    while True:
        value = (yield)
        print("received %s" % value)

listener = handler()
listener.__next__()
listener.send(3)
listener.send('message')