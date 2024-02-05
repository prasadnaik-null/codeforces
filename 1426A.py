#1426A - Floor Number
import re
for i in range(int(input())):
  [n,x]=[int(i) for i in re.split(" ",input())]
  for i in range(n):
    if ((x*i)+2)>=n:
      print(i+1)
      break