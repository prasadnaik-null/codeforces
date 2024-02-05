#1343B - Balanced Array
for i in range(int(input())):
  x,y=int(input()),[]
  if x%4==0:
    print("YES")
    for j in range(1,int(x//2)+1):
      y.append(2*j)
    for j in range(int(x//2)-1):
      y.append((2*j)+1)
    y.append(sum(y[:x//2])-sum(y[x//2:]))
    print(*y)
  else:
    print("NO")