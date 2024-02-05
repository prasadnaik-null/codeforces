# 1303A - Erasing Zeroes
for _ in range(int(input())):
    x = input()
    y = x[::-1]
    if x.count("1") == 0:
        print("0")
    else:
        print(x[x.index("1"):len(x)-y.index("1")].count("0"))