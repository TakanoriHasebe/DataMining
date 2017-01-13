#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 11:09:22 2017

@author: Takanori
"""

"""
TextMinig temp
"""

import MeCab
from collections import Counter
import pyper
import  pandas as pd

s = ["今日は晴れ", "明日も晴れ"]

r=pyper.R(use_pandas='True',use_numpy='True')

r.assign("data", s)

"""
print(r('data'))

r('library(RMeCab)')
r('res = unlist(RMeCabC(data))')
print(r('res'))
#print(r('str(res)'))
print(' ')
p = []

p.append(r('res'))
print(p[0])
"""
