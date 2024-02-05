#1560A - Dislike of Threes
n,x=int(input()),[]
for i in range(n):
  x.append(int(input()))
M,z,y=max(x),1,[]
for i in range(M):
  while True:
    if z%3!=0 and z%10!=3:
      y.append(z)
      z+=1
      break
    z+=1
for i in range(n):
  print(y[x[i]-1])