#1367A - Short Substrings
for i in range(int(input())):
  x=input()
  y=x[:2]
  for j in range(3,len(x),2):
    y+=x[j]
  print(y)