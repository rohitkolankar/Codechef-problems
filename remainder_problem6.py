# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 19:52:24 2021

@author: HP
"""
N=int(input())

for i in range(N):
    (num1,num2)=map(int,input().split(" "))
    print(num1%num2)