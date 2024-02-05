#707A - Brain's Photos
import re
[n,m],x=[int(i) for i in re.split(" ",input())],[]
for i in range(n):
  x+=[i for i in re.split(" ",input())]
if "C" in x or "M" in x or "Y" in x:
  print("#Color")
else:
  print("#Black&White")