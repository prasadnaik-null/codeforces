#1542A - Odd Set
import re
for i in range(int(input())):
  n,x,m=int(input()),[int(i) for i in re.split(" ",input())],0
  for i in x:
    if i%2==0:
      m+=1
  if m==n:
    print("YES")
  else:
    print("NO")