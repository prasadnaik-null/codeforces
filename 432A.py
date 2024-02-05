#432A - Choosing Teams
import re
[n,k],x,s=[int(i) for i in re.split(" ",input())],sorted([int(i) for i in re.split(" ",input())]),0
for i in range(n):
  if x[i]<=5-k:
    s+=1
print(s//3)