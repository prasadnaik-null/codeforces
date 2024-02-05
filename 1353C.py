#1353C - Board Moves
for i in range(int(input())):
  x=int(input())
  a,b,k=x//2,0,1
  for j in range(1,x,2):
    b+=j*k
    k+=1
  print((a*(a+1)*2)+b*4)