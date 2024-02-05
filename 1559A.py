# 1559A - Mocha and Math
for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    x, l = l[0], set(l)
    for i in l:
        x = x & i
    print(x)