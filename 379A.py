#379A - New Year Candles
[n,m]=list(map(int,input().split()))
k=n
while n>=m:
  k+=n//m
  n=n%m+n//m
print(k)