#758A - Holiday Of Equality
import re
n,x,t=int(input()),sorted([int(i) for i in re.split(" ",input())]),0
for i in range(n):
  d=x[-1]-x[i]
  if d>0:
    t+=d
  else:
    break
print(t)