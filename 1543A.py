# 1543A - Exciting Bets
for _ in range(int(input())):
    [a, b] = list(map(int, input().split()))
    z = abs(a-b)
    try:
        x = a-(a//z)*z
        print(z, min(x, z-x))
    except:
        print(0, 0)