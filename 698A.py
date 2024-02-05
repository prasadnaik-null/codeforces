# 698A.py ~ prasadnaik-null
n, a = int(input()), list(map(int, input().split()))
w, r = 3, 0
for i in range(n):
    if a[i] == 1:
        if w == 2:
            r += 1
            w = 3
        else:
            w = 2
    elif a[i] == 2:
        if w == 1:
            r += 1
            w = 3
        else:
            w = 1
    elif a[i] == 0:
        r += 1
        w = 3
    else:
        if w == 1:
            w = 2
        elif w == 2:
            w = 1
        else:
            i0, i1, i2 = n, n, n
            if 1 in a[i:]:
                i1 = a[i:].index(1)
            if 2 in a[i:]:
                i2 = a[i:].index(2)
            if 0 in a[i:]:
                i0 = a[i:].index(0)
            m = min(i0, i1, i2)
            if m == i0:
                w = 2
            elif m == i1:
                if i1 % 2 == 0:
                    w = 2
                else:
                    w = 1
            elif m == i2:
                if i2 % 2 == 0:
                    w = 1
                else:
                    w = 2
print(r)