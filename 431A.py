#431A - Black Square
import re
x,n,t=[int(i) for i in re.split(" ",input())],input(),0
for i in range(4):
  t+=n.count(str(i+1))*x[i]
print(t)