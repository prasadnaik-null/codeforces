#1560B - Who's Opposite?
import re
for i in range(int(input())):
  [a,b,c]=[int(i) for i in re.split(" ",input())]
  d,e=min(a,b),max(a,b)
  f=e-d
  g=f*2
  if d*2<=e and g>=c:
    if c<=f:
      print(f+c)
    else:
      print(c-f)
  else:
    print(-1)