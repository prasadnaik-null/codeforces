#1529A - Eshag Loves Big Arrays
for i in range(int(input())):
  n,x=int(input()),list(map(int,input().split()))
  print(n-x.count(min(x)))