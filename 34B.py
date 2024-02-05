#34B - Sale
[a,b],x=list(map(int,input().split())),sorted(list(map(int,input().split())))
print(-sum(i for i in x[:b] if i<0))