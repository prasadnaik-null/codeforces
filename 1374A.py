#1374A - Required Remainder
import re
for j in range(int(input())):
  [x,y,n]=[int(i) for i in re.split(" ",input())]
  a=n//x
  for i in range(a,-1,-1):
    z=(i*x)+y
    if z<=n:
      print(z)
      break