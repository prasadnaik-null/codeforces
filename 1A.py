#1A - Theatre Square
import re
z=input()
z=re.split(" ",z)
n=int(z[0])
m=int(z[1])
a=int(z[2])
if n%a==0:
  x=int(n/a)
else:
  x=int(n/a)+1
if m%a==0:
  y=int(m/a)
else:
  y=int(m/a)+1
f=x*y
print(f)