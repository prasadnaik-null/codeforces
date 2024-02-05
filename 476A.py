#476A - Dreamoon and Stairs
[a,b],k=list(map(int,input().split())),True
if a%2==1:
  t=(a//2)+1
else:
  t=a//2
while t<=a:
  if t%b==0:
    print(t)
    k=False
    break
  t+=1
if k==True:
  print(-1)