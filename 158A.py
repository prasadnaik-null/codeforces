#VKCupQuali2012A - Next Round
import re
x=input()
x=re.split(" ",x)
y=input()
y=re.split(" ",y)
k=int(x[1])
if int(y[k-1])>0:
  while k<int(x[0]) and y[k-1]==y[k]:
    k+=1
else:
  while int(y[k-1])<=0 and k>0:
    k-=1
print(k)