#1399B - Gifts Fixing
import re
for i in range(int(input())):
  n,x,y,m=int(input()),[int(i) for i in re.split(" ",input())],[int(i) for i in re.split(" ",input())],0
  a,b=min(x),min(y)
  for i in range(n):
    while True:
      if x[i]>a and y[i]>b:
        z=min(x[i]-a,y[i]-b)
        x[i],y[i],m=x[i]-z,y[i]-z,m+z
      elif x[i]>a:
        x[i],m=a,m-a+x[i]
      elif y[i]>b:
        y[i],m=b,m-b+y[i]
      else:
        break
  print(m)