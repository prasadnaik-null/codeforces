#197A - Helpful Maths
import re
x=input()
y=[0,0,0,0]
z=str()
x=re.split("\\+",x)
for i in range(len(x)):
  if x[i]=="1":
    y[1]+=1
  if x[i]=="2":
    y[2]+=1
  if x[i]=="3":
    y[3]+=1
for i in range(y[1]):
  z=z+"1+"
for i in range(y[2]):
  z=z+"2+"
for i in range(y[3]):
  z=z+"3+"
print(z[:-1])