#1341A - Nastya and Rice
for i in range(int(input())):
  [a,b,c,d,e]=list(map(int,input().split()))
  if (b-c)*a<=e+d and (c+b)*a>=d-e:
    print("Yes")
  else:
    print("No")