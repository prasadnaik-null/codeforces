#149A - Business trip
x,y,a,k=int(input()),sorted(list(map(int,input().split())))[::-1],0,True
for i in range(12):
  a+=y[i]
  if a>=x:
    k=False
    if x==0:
      print(0)
      break
    print(i+1)
    break
if k==True:
  print(-1)