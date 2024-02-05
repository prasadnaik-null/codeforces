#1541A - Pretty Permutations
for i in range(int(input())):
  x,y=int(input()),[]
  for j in range(1,x-2,2):
    y.append(j+1)
    y.append(j)
  if x%2==1:
    y.append(x)
    y.append(x-2)
    y.append(x-1)
  else:
    y.append(x)
    y.append(x-1)
  print(*y)