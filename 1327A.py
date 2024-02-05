# 1327A - Sum of Odd Integers
for _ in range(int(input())):
    [a, b] = list(map(int, input().split()))
    x, y = a % 2, b % 2
    if x == y and b*b <= a:
        print("YES")
    else:
        print("NO")