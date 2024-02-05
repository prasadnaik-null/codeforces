#268A - Games
import re
n=int(input())
c=0
x=[]
for i in range(n):
  x.append([int(i) for i in re.split(" ",input())])
for i in range(n):
  for j in range(i):
    if x[i][0]==x[j][1]:
      c+=1
  for j in range(i+1,n):
    if x[i][0]==x[j][1]:
      c+=1
print(c)