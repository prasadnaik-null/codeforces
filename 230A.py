#230A - Dragons
import re
t,x,a,b,c=[int(i) for i in re.split(" ",input())],[],[],[],False
for i in range(t[1]):
  x.append([int(i) for i in re.split(" ",input())])
x=sorted(x)
for i in range(len(x)):
  a.append(x[i][0])
  b.append(x[i][1])
for i in range(t[1]):
  if t[0]+sum(b[:i])>a[i]:
    pass
  else:
    print("NO")
    c=True
    break
if c==False:
  print("YES")