#!/usr/bin/env python

import threading, time, requests

class HTMLGetter(threading.Thread) :
    def __init__(self, url) :
        threading.Thread.__init__(self)
        self.url = url
    def run(self) :
        resp = requests.get(self.url)
        time.sleep(1)
        print(self.url, len(resp.text), 'chars')

t = HTMLGetter('https://google.com')
t.start()

print('### End ###')