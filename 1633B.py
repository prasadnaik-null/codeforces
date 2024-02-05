# 1633B - Minority
for _ in range(int(input())):
    x = input()
    if x.count("1") != x.count("0"):
        print(min(x.count("1"), x.count("0")))
    else:
        print(x.count("1")-1)