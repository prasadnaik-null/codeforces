# 118B - Present from Lena
def func(n, l, k=0):
    print("  "*(n-len(l)+1), end="")
    print(*l,end="")
    if len(l)>1:
        print(" ",end='')
    print(*l[:-1][::-1])
    if k == 0:
        if len(l) <= n:
            l.append(l[-1]+1)
            func(n, l)
        else:
            func(n, l[:-1], 1)
    else:
        if len(l) > 1:
            func(n, l[:-1], 1)


n, l = int(input()), [0]
func(n, l)