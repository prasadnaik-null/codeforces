#1389A - LCM Problem
import re
for i in range(int(input())):
  [l,r]=[int(i) for i in re.split(" ",input())]
  if 2*l<=r:
    print(l,2*l)
  else:
    print(-1,-1)