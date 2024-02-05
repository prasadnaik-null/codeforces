#1360B - Honest Coach
import re
for i in range(int(input())):
  n,x=int(input()),sorted([int(i) for i in re.split(" ",input())])
  m=x[-1]-x[0]
  for j in range(n-1):
    a=x[j+1]-x[j]
    if a<m:
      m=a
  print(m)