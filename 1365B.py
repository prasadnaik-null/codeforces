# 1365B ~ prasadnaik-null
for _ in range(int(input())):
    n, a, b = int(input()), list(map(int, input().split())
                                 ), list(map(int, input().split()))
    if 0 in b and 1 in b:
        print("Yes")
    elif a == sorted(a):
        print("Yes")
    else:
        print("No")