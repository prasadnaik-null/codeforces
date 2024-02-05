# 1420A - Cubes Sorting
for _ in range(int(input())):
    n, l, a ,k= int(input()), list(map(int, input().split())), 0,True
    x=sorted(l)[::-1]
    if l==x:
        if x==list(set(x)):
            print("NO")
        else:
            print("YES")
    else:
        print("YES")