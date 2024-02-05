#1535A - Fair Playoff
import re
for i in range(int(input())):
  x=[int(i) for i in re.split(" ",input())]
  a,b=x.index(max(x)),x.index(sorted(x)[-2])
  if ((a==2 or a==3) and (b==0 or b==1)) or ((a==0 or a==1) and (b==2 or b==3)):
    print("YES")
  else:
    print("NO")