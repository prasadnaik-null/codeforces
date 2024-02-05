#161A - Beautiful Matrix
import re
for i in range(5):
  x=input()
  x=re.split(" ",x)
  for j in range(5):
    if int(x[j])==1:
      y=abs(i-2)+abs(j-2)
      print(y)