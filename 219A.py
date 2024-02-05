# 291A - k-String

n, s, x, k = int(input()), input(), {}, None
for i in s:
    if i not in x:
        y = s.count(i)
        if y % n == 0:
            x[i] = y
        else:
            k = False
            break
if k == False:
    print(-1)
else:
    y = ""
    for i in x:
        y += i*(x[i]//n)
    print(y*n)