#163B - Queue at the School
import re
x=re.split(" ",input())
q=input()
n,t=int(x[0]),int(x[1])
for i in range(t):
  q=re.sub("BG","GB",q)
print(q)