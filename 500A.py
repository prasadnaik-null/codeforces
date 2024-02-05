#50A - New Year Transportation
[n,m],x,p,y=list(map(int,input().split())),list(map(int,input().split())),1,[]
while True:
  if p==m:
    print("YES")
    break
  elif p in y or p>=n:
    print("NO")
    break
  else:
    y.append(p)
  p+=x[p-1]