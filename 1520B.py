#1520B - Ordinary Numbers
for i in range(int(input())):
  x=input()
  y=9*(len(x)-1)
  if int(x[0]*len(x))>int(x):
    y+=int(x[0])-1
  else:
    y+=int(x[0])
  print(y)