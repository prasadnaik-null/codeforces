#233A - Perfect Permutation
n,y=int(input()),[]
if n%2==0:
  for i in range(1,n+1):
    if i%2==0:
      y.append(i-1)
    else:
      y.append(i+1)
  print(*y)
else:
  print(-1)