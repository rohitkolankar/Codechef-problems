# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 19:59:51 2021

@author: HP
"""

N=int(input())

for i in range(N):
    fact=1
    T=int(input())
    for i in range(T):
      fact=fact*T
      T-=1
    print(fact)