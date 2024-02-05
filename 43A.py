#43A - Football
y={}
for i in range(int(input())):
  x=input()
  try:
    y[x]+=1
  except:
    y[x]=1
print(max(y, key=y.get))