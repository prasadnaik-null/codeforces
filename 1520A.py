#1520A - Do Not Be Distracted!
import re
for i in range(int(input())):
  n,x,k,d=int(input()),input(),False,{}
  a=x[0]
  for i in range(n):
    if x[i]==a:
      try:
        d[a]+=1
      except:
        d[a]=1
    else:
      if d[x[i-1]]!=x.count(x[i-1]):
        print("NO")
        k=True
        break
      a=x[i]
      d[a]=1
  if k==False:
    print("YES")