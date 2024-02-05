# 265A - Colorful Stones (Simplified Edition)
s, t, n = input(), input(), 0
for i in range(len(t)):
    if t[i] == s[n]:
        n += 1
print(n+1)