#1385A - Three Pairwise Maximums
import re
for i in range(int(input())):
  x=[int(i) for i in re.split(" ",input())]
  a,b=max(x),min(x)
  if a==b:
    print("YES")
    print(a,a,a)
  elif x.count(a)<=x.count(b):
    print("NO")
  else:
    print("YES")
    print(a,b,1)