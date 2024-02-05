#1619A - Polycarp and Sums of Subsequences
for i in range(int(input())):
  x=sorted(list(map(int,input().split())))
  a,b=x[0],x[1]
  if x[2]==a+b:
    c=x[3]
  else:
    c=x[2]
  print(a,b,c)