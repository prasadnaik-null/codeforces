#405A - Bear and Big Brother
import re
x=input()
x=re.split(" ",x)
i=0
x[0],x[1]=int(x[0]),int(x[1])
while x[0]<=x[1]:
  x[0]=x[0]*3
  x[1]=x[1]*2
  i+=1
print(i)