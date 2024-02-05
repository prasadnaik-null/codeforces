# 1312B - Bogosort
for _ in range(int(input())):
    n = int(input())
    print(*sorted(list(map(int, input().split())))[::-1])