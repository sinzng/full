#!/usr/bin/env python

import threading, time, requests

def getHTML(url) :
    resp = requests.get(url)
    time.sleep(1)
    print(url, len(resp.text), 'chars')
t = threading.Thread(target=getHTML, args=('http://google.com',))
t.start()

print('### End ###')