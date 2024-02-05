#381A - Sereja and Dima
import re
n,x,l=int(input()),[int(i) for i in re.split(" ",input())],[0,0]
for i in range(n):
  a=max(x[0],x[-1])
  l[i%2]+=a
  x.remove(a)
print(*l)