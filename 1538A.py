#1538A - Stone Game
import re
for i in range(int(input())):
  n,x,m=int(input()),[int(i) for i in re.split(" ",input())],0
  a,b=x.index(min(x))+1,x.index(max(x))+1
  c,d=n-a+1,n-b+1
  if min(a,c)<=min(b,d):
    if a<c:
      x=x[a:]
      m+=a
    else:
      x=x[:-c]
      m+=c
    b=x.index(max(x))+1
    m+=min(b,n-b+1-m)
  else:
    if b<d:
      x=x[b:]
      m+=b
    else:
      x=x[:-d]
      m+=d
    a=x.index(min(x))+1
    m+=min(a,n-a+1-m)
  print(m)