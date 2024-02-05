#1353A - Most Unstable Array
import re
for i in range(int(input())):
  [n,m]=[int(i) for i in re.split(" ",input())]
  if n==1:
    print(0)
  elif n==2:
    print(m)
  else:
    print(m*2)