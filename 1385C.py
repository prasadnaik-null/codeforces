for _ in range(int(input())):
    n,l=int(input()),list(map(int,input().split()))[::-1]
    k=True
    s=False
    for i in range(n-1):
        if k==True:
            if l[i]>l[i+1]:
                k=False
        else:
            if l[i]<l[i+1]:
                s=True
                break
    if s==True:
        print(n-i-1)
    else:
        print(0)