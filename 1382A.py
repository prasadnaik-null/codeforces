#1382A - Common Subsequence
for i in range(int(input())):
  x,a,b,k=input(),list(map(int,input().split())),list(map(int,input().split())),True
  for j in a:
    if j in b:
      print("YES")
      print(1,j)
      k=False
      break
  if k==True:
    print("NO")