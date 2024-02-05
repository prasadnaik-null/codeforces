#677A - Vanya and Fence
import re
x=[int(i) for i in re.split(" ",input())]
hh=sorted([int(i) for i in re.split(" ",input())])
if hh[x[0]-1]<=x[1]:
  print(x[0])
else:
  for i in range(x[0]):
    if hh[i]>x[1]:
      print(i+((x[0]-i)*2))
      break