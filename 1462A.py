#1462A - Favorite Sequence
import re
for i in range(int(input())):
  n,x,y=int(input()),[int(i) for i in re.split(" ",input())],[]
  for i in range(n):
    if i%2==0:
      y.append(x[i//2])
    else:
      y.append(x[-((i//2)+1)])
  print(*y)