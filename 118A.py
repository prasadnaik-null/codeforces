#89A - String Task
x=input().lower()
y=str()
for i in range(len(x)):
  if x[i] in ['a','e','i','o','u','y']:
    continue
  else:
    y=y+"."+x[i]
print(y)