#1368A - C+=
for i in range(int(input())):
  [a,b,c]=sorted(list(map(int,input().split())))
  j=0
  while a<=c and b<=c:
    if j%2==0:
      a+=b
    else:
      b+=a
    j+=1
  print(j)