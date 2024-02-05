#1538A - Friends and Candies
for i in range(int(input())):
  n,x=int(input()),list(map(int,input().split()))
  y,c=sum(x)/n,0
  if (y)%1==0:
    for i in x:
      if i>y:
        c+=1
    print(c)
  else:
    print(-1)