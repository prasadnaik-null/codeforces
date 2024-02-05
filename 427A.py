#427A - Police
import re
n,x,m,s=int(input()),[int(i) for i in re.split(" ",input())],0,0
for i in range(n):
  s+=x[i]
  if (s+m)<0:
    m+=1
print(m)