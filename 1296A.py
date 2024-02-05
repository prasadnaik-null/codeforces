#1296A - Array with Odd Sum
import re
for i in range(int(input())):
  n,x=int(input()),[int(i) for i in re.split(" ",input())]
  o,e=0,0
  for j in range(n):
    if x[j]%2==0:
      e+=1
    else:
      o+=1
  if n%2==0 and e!=0 and o!=0:
    print("YES")
  elif n%2==1 and o!=0:
    print("YES")
  else:
    print("NO")