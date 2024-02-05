#1385B - Restore the Permutation by Merger
import re
for i in range(int(input())):
  n,x,y,z=int(input()),[int(i) for i in re.split(" ",input())],[],[]
  for i in range(1,n+1):
    y.append(x.index(i))
  z,a=sorted(y),[]
  for i in range(n):
    a.append(y.index(z[i])+1)
  print(*a)