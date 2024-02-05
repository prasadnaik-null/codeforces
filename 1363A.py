# 1363A - Odd Selection
for _ in range(int(input())):
    [n, x] = list(map(int, input().split()))
    l = list(map(int, input().split()))
    o, e = 0, 0
    for i in l:
        if i % 2 == 0:
            e += 1
        else:
            o += 1
    if n==x:
        if o%2==0:
            print("No")
        else:
            print("Yes")
    elif o==0:
        print("No")
    elif e>=1:
        print("Yes")
    elif x%2==1:
        print("Yes")
    else:
        print("No")