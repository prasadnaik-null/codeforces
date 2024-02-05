#1353B - Two Arrays And Swaps
import re
for i in range(int(input())):
  [n,k]=[int(i) for i in re.split(" ",input())]
  x,y=sorted([int(i) for i in re.split(" ",input())]),sorted([int(i) for i in re.split(" ",input())])[::-1]
  for j in range(k):
    if x[j]<=y[j]:
      x[j]=y[j]
    else:
      break
  print(sum(x))