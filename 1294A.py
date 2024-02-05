#1294A - Collecting Coins
import re
for i in range(int(input())):
  x=[int(i) for i in re.split(" ",input())]
  x,n=x[:3],x[3]
  y=[max(x)-x[i] for i in range(3)]
  if (n-sum(y))>=0 and (n-sum(y))%3==0:
    print("YES")
  else:
    print("NO")