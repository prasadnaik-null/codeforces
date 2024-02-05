#1398A - Bad Triangle
for i in range(int(input())):
  n,x=int(input()),list(map(int,input().split()))
  if x[0]+x[1]<=x[-1]:
    print(1,2,n)
  else:
    print(-1)