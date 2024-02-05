#1537A - Arithmetic Array
for i in range(int(input())):
  x=-int(input())+sum(list(map(int,input().split())))
  if x<0:
    print(1)
  else:
    print(x)