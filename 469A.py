#469A - I Wanna Be the Guy
import re
n,x,t=int(input()),[int(i) for i in re.split(" ",input())][1:]+[int(i) for i in re.split(" ",input())][1:],False
for i in range(1,n+1):
  if i in x:
    continue
  else:
    print("Oh, my keyboard!")
    t=True
    break
if t==False:
  print("I become the guy.")