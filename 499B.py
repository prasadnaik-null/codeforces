#499B - Lecture
[a,b],c=list(map(int,input().split())),{}
for i in range(b):
  [x,y]=list(map(str,input().split()))
  xl,yl=len(x),len(y)
  if xl<=yl:
    c[y]=x
  else:
    c[x]=y
x,y=list(map(str,input().split())),[]
for i in x:
  try:
    y.append(c[i])
  except:
    y.append(i)
print(*y)