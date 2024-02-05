# 1559B - Mocha and Red and Blue
from re import L


for _ in range(int(input())):
    n, s = int(input()), input()
    if "R" in s:
        if "B" in s:
            if s.index("R") < s.index("B"):
                z = s.index("R")
                if z % 2 == 0:
                    s0 = ("RB"*((n//2)+1))[:n]
                    s1 = ("BR"*((n//2)+1))[:n]
                else:
                    s0 = ("BR"*((n//2)+1))[:n]
                    s1 = ("RB"*((n//2)+1))[:n]
            else:
                z = s.index("B")
                if z % 2 == 1:
                    s0 = ("RB"*((n//2)+1))[:n]
                    s1 = ("BR"*((n//2)+1))[:n]
                else:
                    s0 = ("BR"*((n//2)+1))[:n]
                    s1 = ("RB"*((n//2)+1))[:n]
        else:
            z = s.index("R")
            if z % 2 == 0:
                s0 = ("RB"*((n//2)+1))[:n]
                s1 = ("BR"*((n//2)+1))[:n]
            else:
                s0 = ("BR"*((n//2)+1))[:n]
                s1 = ("RB"*((n//2)+1))[:n]
    else:
        if "B" in s:
            z = s.index("B")
            if z % 2 == 1:
                s0 = ("RB"*((n//2)+1))[:n]
                s1 = ("BR"*((n//2)+1))[:n]
            else:
                s0 = ("BR"*((n//2)+1))[:n]
                s1 = ("RB"*((n//2)+1))[:n]
        else:
            s0 = ("RB"*((n//2)+1))[:n]
            s1 = ("BR"*((n//2)+1))[:n]
    d, a = s0, ""
    for i in range(n):
        if s[i] == "?":
            a += d[i]
        elif s[i] == "R":
            if d[i] != "R":
                if d == s0:
                    d = s1
                else:
                    d = s0
            a += "R"
        else:
            if d[i] != "B":
                if d == s0:
                    d = s1
                else:
                    d = s0
            a += "B"
    print(a)