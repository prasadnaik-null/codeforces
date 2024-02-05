#935A - Fafa and his Company
n,m=int(input()),0
for i in range(1,(n//2)+1):
  if n%i==0:
    m+=1
print(m)