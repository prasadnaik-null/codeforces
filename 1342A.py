#1342A - Road To Zero
for i in range(int(input())):
  [a,b],[c,d]=list(map(int,input().split())),list(map(int,input().split()))
  if d<c*2:
    print(d*min(a,b)+c*abs(a-b))
  else:
    print(c*(a+b))