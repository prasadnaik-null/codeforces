#158B - Taxi
import re
import math
n=int(input())
x=[int(i) for i in re.split(" ",input())]
t=0
n=[0]*5
for i in x:
  n[i]+=1
if n[2]%2==0:
  n[2]=n[2]/2
else:
  n[2]=(n[2]//2)+1
  n[1]=n[1]-2
n[1]=n[1]-n[3]
if n[1]<=0:
  n[1]=0
else:
  n[1]=math.ceil(n[1]/4)
print(int(sum(n)))