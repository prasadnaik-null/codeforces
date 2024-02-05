# 1519A - Red and Blue Beans
for i in range(int(input())):
    [a, b, c] = list(map(int, input().split()))
    m = max(a/b, b/a)
    if m != int(m):
        m = int(m)+1
    if m-1 <= c:
        print("YES")
    else:
        print("NO")