#1352A - Sum of Round Numbers
for i in range(int(input())):
  x,y=input(),[]
  for j in range(len(x)):
    z=x[j]+'0'*(len(x)-j-1)
    if int(z)!=0:
      y.append(z)
  print(len(y))
  print(*y)