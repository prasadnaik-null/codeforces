#577A - Multiplication Table
[a,b],m,k=list(map(int,input().split())),0,True
for i in range(1,a+1):
  if i**2>b:
    break
  if (b/i)%1==0 and b/i<=a:
    m+=1
x=b**0.5
if x%1==0 and x<=a:
  print((m*2)-1)
else:
  print(m*2)