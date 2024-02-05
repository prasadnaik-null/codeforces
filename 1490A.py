#1490A - Dense Array
import math
for i in range(int(input())):
  n,x,m=int(input()),list(map(int,input().split())),0
  for i in range(n-1):
    if x[i]>x[i+1] and x[i]/x[i+1]>2:
        m+=math.ceil(math.log(x[i]/x[i+1],2)-1)
    elif x[i+1]>x[i] and x[i+1]/x[i]>2:
        m+=math.ceil(math.log(x[i+1]/x[i],2)-1)
  print(m)