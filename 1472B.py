#1472B - Fair Division
import re
for i in range(int(input())):
  n,x=int(input()),[int(i) for i in re.split(" ",input())]
  a,b=x.count(1),x.count(2)
  if (a!=0 and x.count(1)%2==0) or (a==0 and b%2==0):
    print("YES")
  else:
    print("NO")