#584A - Olesya and Rodion
[a,b],k=list(map(int,input().split())),False
for i in range(10**(a-1),(10**a)):
  if i%b==0:
    print(i)
    k=True
    break
if k==False:
  print("-1")