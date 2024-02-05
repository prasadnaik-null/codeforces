#1472A - Cards for Friends
import re
import math
def f2(n):
  m=0
  while True:
    if n%2==0:
      m+=1
      n//=2
    else:
      return m

for i in range(int(input())):
  [w,h,n]=[int(i) for i in re.split(" ",input())]
  a=f2(w)+f2(h)
  if 2**a>=n:
    print("YES")
  else:
    print("NO")