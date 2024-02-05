#1619A - Square String?
for i in range(int(input())):
  x=input()
  z=len(x)/2
  if z%1==0 and x[:int(z)]==x[int(z):]:
    print("YES")
  else:
    print("NO")