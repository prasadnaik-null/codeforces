# 349A - Cinema Line
n, l = int(input()), list(map(int, input().split()))
c25, c50, k = 0, 0, True
for i in range(n):
    if l[i] == 25:
        c25 += 1
    elif l[i] == 50:
        if c25 > 0:
            c25 -= 1
            c50 += 1
        else:
            k = False
            break
    else:
        if c50 > 0 and c25 > 0:
            c50 -= 1
            c25 -= 1
        elif c25 > 2:
            c25 -= 3
        else:
            k = False
            break
if k == True:
    print("YES")
else:
    print("NO")