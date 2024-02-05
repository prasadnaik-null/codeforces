# 1077A - Frog Jumping
for _ in range(int(input())):
    [a, b, k] = list(map(int, input().split()))
    z = k//2
    print(a*(k-z)-b*z)