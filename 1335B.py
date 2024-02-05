#1335B - Construct the String
for i in range(int(input())):
  [n,a,b],i,x=list(map(int,input().split())),0,str()
  b=min(b,26)
  for i in range(n):
    x+=chr(97+(i%b))
  print(x)