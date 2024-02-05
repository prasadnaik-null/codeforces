#479A - Wrong Subtraction
import re
x=re.split(" ",input())
n,k=int(x[0]),int(x[1])
for i in range(k):
  if n%10==0:
    n=int(n/10)
  else:
    n-=1
print(n)