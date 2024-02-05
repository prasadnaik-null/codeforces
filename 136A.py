#136A - Presents
import re
n=int(input())
x=[int(i) for i in re.split(" ",input())]
y=[None]*n
for i in range(n):
  y[x[i]-1]=i+1
print(*y)