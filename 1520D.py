# 1520D - Same Differences
def ans(x):
    return (x*(x-1))//2


for _ in range(int(input())):
    n, l = int(input()), list(map(int, input().split()))
    d = {}
    dm = {}
    a = 0
    for i in range(n):
        x = l[i]-i
        if x >= 0:
            try:
                d[x] += 1
            except:
                d[x]=1
        else:
            try:
                dm[x] += 1
            except:
                dm[x]=1
    d=list(d.values())
    dm=list(dm.values())
    for i in d:
        a+=ans(i)
    for i in dm:
        a+=ans(i)
    print(a)