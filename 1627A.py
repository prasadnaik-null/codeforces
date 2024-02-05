# 1627A - Not Shading
for _ in range(int(input())):
    [n, m, r, c], l, b = list(map(int, input().split())), [], False
    for i in range(n):
        x = input()
        l.append(x)
        if b == False and "B" in x:
            b = True
    if b == False:
        print(-1)
    else:
        if l[r-1][c-1] == "B":
            print(0)
        elif "B" in l[r-1]:
            print(1)
        else:
            k = False
            for i in l:
                if i[c-1] == "B":
                    print(1)
                    k = True
                    break
            if k == False:
                print(2)