# 1256A - Payment Without Change
for _ in range(int(input())):
    [a, b, n, s] = list(map(int, input().split()))
    if a*n < s:
        if b >= s-(a*n):
            print("YES")
        else:
            print("NO")
    else:
        if b >= s % n:
            print("YES")
        else:
            print("NO")