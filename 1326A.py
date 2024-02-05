# 1326A - Bad Ugly Numbers
for _ in range(int(input())):
    x = int(input())
    if x == 1:
        print(-1)
    else:
        if (x-1) % 3 == 0:
            print(("2"*(x-2))+"33")
        else:
            print(("2"*(x-1))+"3")