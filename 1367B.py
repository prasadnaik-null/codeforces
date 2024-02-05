#1367B - Even Array
import re
for i in range(int(input())):
  n,x,a1,a2=int(input()),[int(i) for i in re.split(" ",input())],0,0
  for i in range(0,n,2):
    if x[i]%2!=0:
      a1+=1
  for i in range(1,n,2):
    if x[i]%2!=1:
      a2+=1
  if a1==a2:
    print(a1)
  else:
    print(-1)