#977C ~ prasadnaik-null
[n,m]=list(map(int, input().split()))
y=sorted(list(map(int,input().split())))
x=y[m-1]
if m==0:
    if y[0]>1:
        print(1)
    else:
        print(-1)
elif m==n:
    print(y[-1])
elif y[m-1]==y[m]:
    print(-1)
else:
    print(y[m-1])