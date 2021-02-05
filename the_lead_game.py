# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 19:35:05 2021

@author: HP
"""

n=int(input())

s=0
l=0
lst=[]

for i in range(n):
    (a,b)=map(int,input().split(" "))
    s=s+a
    l=l+b
    if s>l:
        lead=s-l
        lst.append((lead,1))
    else:
        lead=l-s
        lst.append((lead,2))
        
lst.sort(reverse=True)
print(lst)
#print(lst[0][1])
#print(lst[0][0])


