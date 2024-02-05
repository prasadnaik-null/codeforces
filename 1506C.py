# 1506C - Double-ended Strings
for _ in range(int(input())):
    a, b, c, ans = input(), input(), 0, 0
    for i in range(len(a)):
        c = 0
        for j in range(i + 1, len(a)+1):
            if a[i:j] in b:
                c += 1
                ans = max(c, ans)
            else:
                ans = max(c, ans)
                break
    print(len(a)+len(b)-2*ans)