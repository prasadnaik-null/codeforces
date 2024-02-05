#1374B - Multiply by 2, divide by 6
import math
for i in range(int(input())):
  y,m=int(input()),0
  while True:
    y/=6
    if y%1!=0:
      y*=6
      break
    m+=1
  z=round(math.log(y,3),14)
  if z%1==0:
    print(m+int(z*2))
  else:
    print(-1)