#1624A - Plus One on the Subset
import re
for i in range(int(input())):
  n,x=int(input()),[int(i) for i in re.split(" ",input())]
  print(max(x)-min(x))