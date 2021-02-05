# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 19:52:41 2021

@author: HP
"""

N=int(input())

for i in range(N):
    num=list(map(int,input().split(" ")))
    num.sort()
    print(num[-2])