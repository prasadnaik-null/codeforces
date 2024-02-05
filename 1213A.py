# 1213A - Chips Moving
n, l, e, o = int(input()), list(map(int, input().split())), 0, 0
for i in l:
    if i % 2 == 0:
        e += 1
    else:
        o += 1
if o > e:
    print(e)
else:
    print(o)