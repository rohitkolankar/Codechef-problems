# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 20:25:54 2021

@author: HP
"""

N=int(input())

for i in range(N):
    T=list(map(int,input()))
    print(T[0]+T[-1])