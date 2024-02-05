#91A - Lucky Division
n=int(input())
i=2
d=int()
k=False
while int(d)<=n:
  m=bin(i)[3:]
  d=str()
  for j in range(len(m)):
    if m[j]=="0":
      d=d+"4"  
    else:
      d=d+"7"
  d=int(d)
  if n%d==0:
    print("YES")
    k=True
    break
  i+=1
if k==False:
  print("NO")