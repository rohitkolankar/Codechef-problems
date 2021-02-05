# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 19:44:35 2021

@author: HP
"""

N=int(input())

for i in range(N):
    num=input("Num")
    num1=list(map(int,str(num)))
    print(sum(num1))