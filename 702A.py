#702A - Maximum Increase
n,x,m,o=int(input()),list(map(int,input().split())),1,1
for i in range(n-1):
  if x[i]<x[i+1]:
    m+=1
    if o<m:
      o=m
  else:
    m=1
print(o)