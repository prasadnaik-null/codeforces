#84A - Nearly Lucky Number
x=input()
n=0
for i in range(len(x)):
  if x[i]=="4" or x[i]=="7":
    n+=1
if n==4 or n==7:
  print("YES")
else:
  print("NO")