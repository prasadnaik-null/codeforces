# 1469B - Red and Blue
for _ in range(int(input())):
    r, rl, rll, mr = int(input()), list(map(int, input().split())), [0], 0
    b, bl, bll, mb = int(input()), list(map(int, input().split())), [0], 0
    for i in range(r):
        rll.append(rll[-1]+rl[i])
        if mr < rll[-1]:
            mr = rll[-1]
    for j in range(b):
        bll.append(bll[-1]+bl[j])
        if mb < bll[-1]:
            mb = bll[-1]
    print(mr+mb)