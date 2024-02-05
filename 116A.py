#87A - Tram
import re
n=int(input())
j,m=0,0
for i in range(n):
  x=re.split(" ",input())
  j=j-int(x[0])+int(x[1])
  if j>m:
    m=j
print(m)