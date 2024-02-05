#1506A - Strange Table
for i in range(int(input())):
  [n,m,x]=list(map(int,input().split()))
  print(((x-1)//n)+1+m*((x-1)%n))