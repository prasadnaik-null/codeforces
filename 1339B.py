#1339B ~ prasadnaik-null
for _ in range(int(input())):
    n,a=int(input()),sorted(list(map(int,input().split())))
    l=[]
    for i in range(n):
        if i%2==0:
            l.append(a[n-i//2-1])
        else:
            l.append(a[i//2])
    print(*l[::-1],sep=" ")