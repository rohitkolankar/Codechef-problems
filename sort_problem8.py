# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 20:10:15 2021

@author: HP
"""

N=int(input())
lst=[]
for i in range(N):
    X = int(input())
    lst.append(X)
    
lst.sort()

for i in lst:
    print(i)
    