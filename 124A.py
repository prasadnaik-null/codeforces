#124A - The number of positions
[a,b,c]=list(map(int,input().split()))
if b+1>=a-c:
  print(a-b)
else:
  print(c+1)