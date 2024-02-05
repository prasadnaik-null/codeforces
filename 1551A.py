#1551A - Polycarp and Coins
for i in range(int(input())):
  x=int(input())
  y=x//3
  if x%3==0:
    print(y,y)
  elif x%3==1:
    print(y+1,y)
  else:
    print(y,y+1)