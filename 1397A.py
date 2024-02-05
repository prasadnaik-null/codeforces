#1397A - Juggling Letters
for i in range(int(input())):
  x,n=str(),int(input())
  for j in range(n):
    x+=input()
  x=sorted(x)
  k=0
  if n==1:
    print("YES")
  else:
    while k<len(x):
      if x.count(x[k])%n!=0:
        print("NO")
        k=True
        break
      k+=x.count(x[k])
    if k!=True:
      print("YES")