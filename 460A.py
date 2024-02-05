#460A - Vasya and Socks
[n,m],d=list(map(int,input().split())),0
while n>=1:
  n-=1
  d+=1
  if d%m==0:
    n+=1
print(d)