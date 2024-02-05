#1549A - Gregor and Cryptography
for i in range(int(input())):
  x,y=int(input()),{}
  for i in range(2,x+1):
    r=x%i
    try:
      y[r]+=[i]
      if len(y[r])==2:
        print(*y[r])
        break
    except:
      y[r]=[i]