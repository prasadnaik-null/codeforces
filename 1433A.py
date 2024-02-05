#1433A - Boring Apartments
for i in range(int(input())):
  x=input()
  a,b=int(x[0])-1,len(x)
  print(10*(a)+(b*(b+1))//2)