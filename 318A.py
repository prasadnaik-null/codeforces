#318A - Even Odds
import re
x=[int(i) for i in re.split(" ",input())]
if x[0]%2==0:
  if x[1]<=x[0]/2:
    print(int((x[1]*2)-1))
  else:
    print(int((x[1]-(x[0]/2))*2))
else:
  if x[1]<=(x[0]//2)+1:
    print(int((x[1]*2)-1))
  else:
    print(int((x[1]-((x[0]//2)+1))*2))