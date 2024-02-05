# 1398B - Substring Removal Game
for _ in range(int(input())):
    s, f, l, x, a = input(), -1, -1, [], 0
    for i in range(len(s)):
        if s[i] == "1":
            if f == -1:
                f, l = i, i
            else:
                l += 1
        else:
            if f != -1:
                x.append(l-f+1)
                f, l = -1, -1
        if i == len(s)-1:
            if s[i] == "1":
                x.append(l-f+1)
    for i in range(len(x)):
        if i % 2 == 0:
            a += max(x)
        x.remove(max(x))
    print(a)