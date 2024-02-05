# 519B - A and B and Compilation Errors
n, a, b, c = int(input()), sorted(list(map(int, input().split()))), sorted(
    list(map(int, input().split()))), sorted(list(map(int, input().split())))
for i in range(n):
    try:
        if a[i] != b[i]:
            print(a[i])
            break
    except:
        print(a[n-1])
for i in range(n-1):
    try:
        if b[i] != c[i]:
            print(b[i])
            break
    except:
        print(b[n-2])