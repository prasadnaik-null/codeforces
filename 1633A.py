# 1633A - Div. 7
for i in range(int(input())):
    x = int(input())
    m, d = x % 7, x//10
    if (x-m)//10 == d:
        print(x-m)
    else:
        print(x+7-m)