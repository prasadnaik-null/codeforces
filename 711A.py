#711A - Bus to Udayland
k,y=True,[]
for i in range(int(input())):
  [a,b]=list(map(str,input().split("|")))
  if k==True:
    if a=="OO":
      k=False
      a="++"
    elif b=="OO":
      k=False
      b="++"
  y.append(a)
  y.append(b)
if k==False:
  print("YES")
  for i in range(0,len(y),2):
    print(y[i]+"|"+y[i+1])
else:
  print("NO")