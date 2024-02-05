# 1395A - Boboniu Likes to Color Balls
for _ in range(int(input())):
    l, o = list(map(int, input().split())), 0
    for i in l:
        if i % 2 == 1:
            o += 1
    if o > 1:
        if l[0] > 0 and l[1] > 0 and l[2] > 0:
            l[0], l[1], l[2], l[3], o = l[0]-1, l[1]-1, l[2]-1, l[3]+3, 0
            for i in l:
                if i % 2 == 1:
                    o += 1
            if o > 1:
                print("No")
            else:
                print("Yes")
        else:
            print("No")
    else:
        print("Yes")