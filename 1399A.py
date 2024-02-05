#1399A - Remove Smallest
import re
for i in range(int(input())):
  n,x,m=int(input()),sorted([int(i) for i in re.split(" ",input())]),0
  x=[x[0]]+x
  for j in range(n):
    if abs(x[j+1]-x[j])>1:
      m+=1
      break
  if m==0:
    print("YES")
  else:
    print("NO")