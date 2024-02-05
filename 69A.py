#63A - Young Physicist
import re
n=int(input())
x,y,z=0,0,0
for i in range(n):
  a=input()
  a=re.split(" ",a)
  x+=int(a[0])
  y+=int(a[1])
  z+=int(a[2])
if x==0 and y==0 and z==0:
  print("YES")
else:
  print("NO")