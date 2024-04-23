#!/usr/bin/env python


import pandas as pd

filename = 'memberinfo.csv'
df = pd.read_csv(filename)
print(df)