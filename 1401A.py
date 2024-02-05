# 1401A - Distance and Axis
for _ in range(int(input())):
    [n, k] = list(map(int, input().split()))
    if n >= k:
        if (n % 2 == 0 and k % 2 == 0) or (n % 2 == 1 and k % 2 == 1):
            print(0)
        else:
            print(1)
    else:
        print(k-n)