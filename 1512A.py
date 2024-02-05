#1512A - Spy Detected!
import re
for i in range(int(input())):
  n,x=int(input()),[int(i) for i in re.split(" ",input())]
  for j in range(n):
    if x.count(x[j])==1:
      print(j+1)
      break