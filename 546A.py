#304A - Soldier and Bananas
import re
x=input()
x=re.split(" ",x)
k,n,w=int(x[0]),int(x[1]),int(x[2])
ts=int((w*(w+1)/2)*k)
b=ts-n
if b<0:
  b=0
print(b)