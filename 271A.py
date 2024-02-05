#271A - Beautiful Year
y=int(input())
while True:
  y+=1
  y=str(y)
  if y[0]!=y[1] and y[0]!=y[2] and y[0]!=y[3] and y[1]!=y[2] and y[1]!=y[3] and y[2]!=y[3]:
    print(y)
    break
  else:
    y=int(y)