# 1650B - DIV + MOD
for _ in range(int(input())):
    [l, r, a] = list(map(int, input().split()))
    q = r//a
    x = (q)*a-1
    if r % a == a-1 or l > x:
        print((q)+(r % a))
    else:
        print(q+a-2)