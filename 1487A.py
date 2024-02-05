# 1487A - Arena
for _ in range(int(input())):
    x, y = int(input()), list(map(int, input().split()))
    print(x-y.count(min(y)))