# 1312A - Two Regular Polygons
for _ in range(int(input())):
    [n, m] = list(map(int, input().split()))
    if n % m == 0:
        print("YES")
    else:
        print("NO")