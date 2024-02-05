#111A - Twins
import re
n=int(input())
x=sorted([int(i) for i in re.split(" ",input())])[::-1]
s,ss=sum(x),0
for i in range(n):
  ss=ss+x[i]
  if ss>s/2:
    print(i+1)
    break