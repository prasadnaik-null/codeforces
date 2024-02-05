#1348A - Phoenix and Balance
for i in range(int(input())):
  x,y=int(input()),[]
  for i in range(1,x+1):
    y.append(2**i)
  print(sum(y[:(x//2)-1])+y[-1]-sum(y[(x//2)-1:-1]))