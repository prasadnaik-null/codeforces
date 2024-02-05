#490A - Team Olympiad
import re
n,x,t,y=int(input()),[int(i) for i in re.split(" ",input())],0,[]
[a,b,c]=[x.count(1),x.count(2),x.count(3)]
while True:
  if a>0 and b>0 and c>0:
    t+=1
    [d,e,f]=[x.index(1),x.index(2),x.index(3)]
    y.append([d+1,e+1,f+1])
    x[d],x[e],x[f]=0,0,0
    a,b,c=a-1,b-1,c-1
  else: 
    break
print(t)
for i in range(t):
  print(*y[i])