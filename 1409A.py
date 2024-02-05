#1409A - Yet Another Two Integers Problem
import re
for i in range(int(input())):
  x,m,k=[int(i) for i in re.split(" ",input())],0,False
  n=x[1]-x[0]
  m=abs(n)//10
  if x[0]!=x[1]:
    x[0]=x[0]+(abs(n)/n)*m*10
  if x[0]==x[1]:
      print(m)
  else:
    print(m+1)