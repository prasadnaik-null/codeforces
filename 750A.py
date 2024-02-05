#750A - New Year and Hurry
import re
[n,k]=[int(i) for i in re.split(" ",input())]
t,T,k=240-k,0,True
for i in range(1,n+1):
  T+=5*i
  if T>t:
    print(i-1)
    k=False
    break
if k==True:
  print(n)