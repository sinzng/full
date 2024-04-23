#!/usr/bin/env python

import threading
def example():
    for _ in range(1, 15):
        print(_)

example()
example()

threading.Thread(target=example).start()
threading.Thread(target=example).start()
