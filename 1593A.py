#1593A - Elections
for i in range(int(input())):
  [a,b,c]=list(map(int,input().split()))
  x=[a,b,c]
  m=max(a,b,c)+1
  if x.count(m-1)==1:
    if a==m-1:
      print(0,m-b,m-c)
    elif b==m-1:
      print(m-a,0,m-c)
    else:
      print(m-a,m-b,0)
  else:
    print(m-a,m-b,m-c)