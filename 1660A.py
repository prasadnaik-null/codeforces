# 1660A - Vasya and Coins
for _ in range(int(input())):
    [o, t] = list(map(int, input().split()))
    if o == 0:
        print(1)
    else:
        print((2*t)+o+1)