# 1593B - Make it Divisible by 25
for _ in range(int(input())):
    n = input()[::-1]
    a = len(n)
    b, c, d = a, a, a
    if n.count("0") > 1:
        try:
            a = n.index("0")+n[n.index("0")+1:].index("0")
        except:
            pass
    if n.count("0") > 0 and n.count("5") > 0:
        try:
            b = n.index("0")+n[n.index("0")+1:].index("5")
        except:
            pass
    if n.count("2") > 0 and n.count("5") > 0:
        try:
            c = n.index("5")+n[n.index("5")+1:].index("2")
        except:
            pass
    if n.count("7") > 0 and n.count("5") > 0:
        try:
            d = n.index("5")+n[n.index("5")+1:].index("7")
        except:
            pass
    print(min(a, b, c, d))