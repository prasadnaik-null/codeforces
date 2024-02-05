#1521A - Nastia and Nearly Good Numbers
for i in range(int(input())):
  [a,b]=list(map(int,input().split()))
  c=a*b
  x=a
  y=a*(2*b-1)
  z=x+y
  if x%c==0 or y%c==0:
    print("NO")
  else:
    print("YES")
    print(x,y,z)