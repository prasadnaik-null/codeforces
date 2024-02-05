# 1409B - Minimum Product
for _ in range(int(input())):
    [a, b, x, y, n] = list(map(int, input().split()))
    if a-x+b-y <= n:
        print(x*y)
    else:
        if x <= y:
            if a-x <= n:
                n -= a-x
                a = x
                if b-y <= n:
                    b = y
                else:
                    b -= n
            else:
                if a <= b:
                    a -= n
                else:
                    if b-y >= n:
                        b -= n
                    else:
                        if a-y > n:
                            n -= b-y
                            b = y
                        a -= n
        else:
            if b-y <= n:
                n -= b-y
                b = y
                if a-x <= n:
                    a = x
                else:
                    a -= n
            else:
                if b <= a:
                    b -= n
                else:
                    if a-x >= n:
                        a -= n
                    else:
                        if b-x > n:
                            n -= a-x
                            a = x
                        b -= n
        print(a*b)