#1433B - Yet Another Bookshelf
import re
for i in range(int(input())):
  x,n,a=int(input()),list(map(int,input().split())),0
  m=n[::-1]
  for i in n[n.index(1):x-m.index(1)-1]:
    if i==0:
      a+=1
  print(a)