# 1519B - The Cake Is a Lie
for i in range(int(input())):
    [a, b, c] = list(map(int, input().split()))
    if a*(b-1)+a-1 == c:
        print("YES")
    else:
        print("NO")