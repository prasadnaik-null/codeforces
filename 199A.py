# 199A - Hexadecimal's theorem
x, s, n0, n1, n, nn = int(input()), [0, 1], 0, 1, 1, 1
if x < 5:
    if x == 0:
        print("0 0 0")
    elif x == 1:
        print("0 0 1")
    elif x == 2:
        print("0 1 1")
    else:
        print("1 1 1")
else:
    while n < x:
        n = n0+n1
        s.append(n)
        n0, n1 = n1, n
        nn += 1
    print(s[nn-4], s[nn-3], s[nn-1])