#977B - Two-gram
n,x,d=int(input()),input(),{}
for i in range(n-1):
  try:
    d[x[i:i+2]]+=1
  except:
    d[x[i:i+2]]=1
print(sorted(d.items(), key=lambda x: x[1], reverse=True)[0][0])