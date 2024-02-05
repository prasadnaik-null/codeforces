# 1512B - Almost Rectangle
for _ in range(int(input())):
    n, s, c, d = int(input()), [], 0, ""
    for i in range(n):
        x = input()
        if x.count("*") == 1:
            s.append((i, x.index("*")))
            c += 1
            if c == 2:
                s.sort()
                for j in range(n):
                    if j != s[0][0] and j != s[1][0]:
                        print("."*n)
                    else:
                        if j == s[0][0]:
                            if s[0][1] == s[1][1]:
                                if s[0][1] == 0:
                                    d += "**"
                                    for _ in range(n-2):
                                        d += "."
                                else:
                                    d += "*"
                                    for i in range(1, n):
                                        if i == s[0][1]:
                                            d += "*"
                                        else:
                                            d += "."
                            else:
                                for i in range(n):
                                    if i == s[0][1] or i == s[1][1]:
                                        d += "*"
                                    else:
                                        d += "."
                            print(d)
                        else:
                            print(d)
        elif x.count("*") == 2:
            if i != 0:
                print(x)
                for j in range(1, n):
                    if j != i:
                        print("."*n)
                    else:
                        print(x)
            else:
                print(x)
                print(x)
                for _ in range(n-2):
                    print("."*n)