#146A - Boy or Girl
x=input()
y=[]
for i in range(len(x)):
  if x[i] in y:
    continue
  else:
    y.append(x[i])
if len(y)%2==0:
  print("CHAT WITH HER!")
else:
  print("IGNORE HIM!")