#155A - I_love_%username%
import re
n,x=int(input()),[int(i) for i in re.split(" ",input())]
m,M,a=x[0],x[0],0
for i in range(1,n):
  if x[i]>M:
    a,M=a+1,x[i]
  elif x[i]<m:
    a,m=a+1,x[i]
print(a)