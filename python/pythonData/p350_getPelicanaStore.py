#!/usr/bin/env python

from itertools import count
from p340_ChickentUtil import ChickenStore

brandName = 'pelicana'
base_url = 'https://www.pelicana.kr/store/W'

def getData():
    savaData = []

    for page_idx in count():
        url =- base_url + '?page=' + str(page_idx+1)
        chickenStore = ChickenStore(brandName, url)
        soup = chickenStore.getSoup()z
