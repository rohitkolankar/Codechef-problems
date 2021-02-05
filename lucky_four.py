# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 20:33:04 2021

@author: HP
"""

N=int(input())
count=0
for i in range(N):
    lst=map(int,input())
    for num in lst:
        if num==4:
            count+=1
    print(count)
            